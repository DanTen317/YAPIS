from dataclasses import dataclass, field
from typing import Tuple, Any, List, Optional, Dict
from gen.ListLangParserVisitor import ListLangParserVisitor
from gen.ListLangParser import ListLangParser


@dataclass
class Type:
    name: str
    params: Tuple[Any, ...] = ()

    def __str__(self):
        if self.params:
            return f"{self.name}<{', '.join(map(str, self.params))}>"
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Type):
            return False
        # Простая эквивалентность. Для element (Any) можно усложнить
        if self.name == "element" or other.name == "element":
            return True
        return self.name == other.name and self.params == other.params


# PRIMITIVES
ELEMENT = Type("element")  # Generic type
VOID = Type("void")
INT = Type("int")
FLOAT = Type("float")
BOOL = Type("bool")
STR = Type("string")
LIST = Type("list")  # Generic list container
TREE = Type("tree")  # Generic tree container


def get_literal_type(ctx: ListLangParser.LiteralContext) -> Type:
    if ctx.DECIMAL_INTEGER(): return INT
    if ctx.FLOAT_NUMBER(): return FLOAT
    if ctx.STRING(): return STR
    if ctx.BOOLEAN(): return BOOL
    if ctx.OPEN_BRACKET(): return LIST  # Empty list []
    return ELEMENT


@dataclass
class Symbol:
    name: str
    sym_type: Type
    kind: str  # func, param, var
    # Для функций: список аргументов (имя, тип, модификатор доступа)
    params: List[Tuple[str, Type, str]] = field(default_factory=list)
    return_type: Optional[Type] = None
    is_ref: bool = False  # Для параметров передаваемых по ссылке (&)


class Scope:
    def __init__(self, parent: Optional["Scope"] = None) -> None:
        self.parent = parent
        self.table: Dict[str, Symbol] = {}

    def define(self, symbol: Symbol) -> None:
        if symbol.name in self.table:
            # В требованиях сказано про неявное объявление,
            # но повторное объявление в той же области видимости обычно допустимо как обновление
            pass
        self.table[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        s = self
        while s:
            if name in s.table:
                return s.table[name]
            s = s.parent
        return None


class SemanticError(Exception):
    def __init__(self, msg, ctx=None) -> None:
        line_info = ""
        if ctx:
            token = ctx.start
            line_info = f" [line {token.line}:{token.column}]"
        super().__init__(f"{msg}{line_info}")


class SemanticAnalyser(ListLangParserVisitor):
    def __init__(self):
        self.global_scope = Scope(None)
        self.current_scope = self.global_scope
        self.current_function: Optional[Symbol] = None
        self._register_builtins()

    def _register_builtins(self):
        # Встроенные функции ввода-вывода
        self.global_scope.define(Symbol("read", STR, "func", [], STR))
        # write(element...) -> void (variadic arguments logic is custom inside visitAtom)
        self.global_scope.define(Symbol("write", VOID, "func", [("args", ELEMENT, "")], VOID))

        # Конструкторы типов
        self.global_scope.define(Symbol("list", LIST, "func", [], LIST))
        self.global_scope.define(Symbol("tree", TREE, "func", [], TREE))

    def analyse(self, tree):
        return self.visit(tree)

    def enter_scope(self):
        self.current_scope = Scope(self.current_scope)

    def leave_scope(self):
        self.current_scope = self.current_scope.parent

    # --- Visitor Methods ---

    def visitProgram(self, ctx: ListLangParser.ProgramContext):
        # Программа - это глобальная область видимости
        return self.visitChildren(ctx)

    def visitFunc_decl(self, ctx: ListLangParser.Func_declContext):
        func_name = ctx.NAME().getText()

        # Сбор параметров
        params = []
        if ctx.parameter_list():
            # Ручной обход parameter_list, так как нам нужны данные, а не просто visit
            for param_ctx in ctx.parameter_list().param():
                p_name = param_ctx.NAME().getText()
                p_is_ref = param_ctx.AMP() is not None
                # Тип параметра неизвестен при объявлении (динамическая типизация/inference), 
                # ставим ELEMENT
                params.append((p_name, ELEMENT, p_is_ref))

        # Определяем символ функции в текущем (глобальном или родительском) scope
        func_symbol = Symbol(func_name, VOID, "func", params, VOID)
        try:
            self.current_scope.define(func_symbol)
        except SemanticError as e:
            raise SemanticError(f"Function redefinition: {e}", ctx)

        # Входим в scope функции
        self.current_function = func_symbol
        self.enter_scope()

        # Регистрируем параметры как локальные переменные
        for p_name, p_type, p_ref in params:
            self.current_scope.define(Symbol(p_name, p_type, "param", is_ref=p_ref))

        # Посещаем тело
        self.visit(ctx.suite())

        # Выходим
        self.leave_scope()
        self.current_function = None

    def visitReturn_stmt(self, ctx: ListLangParser.Return_stmtContext):
        # Проверка: return только внутри функции
        if self.current_function is None:
            raise SemanticError("Return statement outside of function", ctx)

        # Обработка выражений
        if ctx.expression_list():
            expr_types = []
            for expr in ctx.expression_list().expression():
                expr_types.append(self.visit(expr))

            # Если это первый return, который мы встретили, можем "вывести" тип возврата функции
            # Но пока у нас тип VOID по умолчанию, просто обновляем его
            # (Для полноценного вывода типов нужно сложнее)
            if len(expr_types) == 1:
                self.current_function.return_type = expr_types[0]
            else:
                # Возврат кортежа пока не поддерживаем в типах явно, пусть будет ELEMENT
                self.current_function.return_type = ELEMENT

        return VOID

    def visitAssignment_stmt(self, ctx: ListLangParser.Assignment_stmtContext):
        # target_list = expression_list

        # 1. Вычисляем типы выражений справа
        expr_types = []
        if ctx.expression_list():
            for expr in ctx.expression_list().expression():
                expr_types.append(self.visit(expr))

        # 2. Получаем имена переменных слева
        target_names = [t.getText() for t in ctx.target_list().NAME()]

        # Валидация количества (a, b = 1, 2)
        if len(target_names) != len(expr_types):
            raise SemanticError(f"Assignment mismatch: {len(target_names)} targets but {len(expr_types)} expressions",
                                ctx)

        # 3. Неявное объявление или обновление типов
        for name, expr_type in zip(target_names, expr_types):
            symbol = self.current_scope.resolve(name)
            if symbol is None:
                # Неявное объявление
                # Если переменной с таким именем нет в доступных областях видимости,
                # мы считаем, что это ОБЪЯВЛЕНИЕ новой переменной.
                new_sym = Symbol(name, expr_type, "var")
                self.current_scope.define(new_sym)
            else:
                # Если переменная есть (была объявлена ранее), то обновляем её тип.
                symbol.sym_type = expr_type

    def visitExpression(self, ctx: ListLangParser.ExpressionContext):
        # Рекурсивный обход выражений

        # 1. Унарный NOT (!expr)
        if ctx.NOT():
            res_type = self.visit(ctx.expression(0))
            if res_type != BOOL and res_type != ELEMENT:
                print(f"Warning: Implicit cast to bool in NOT expression [line {ctx.start.line}]")
            return BOOL

        # 2. Атом (переменная, литерал, вызов)
        if ctx.atom():
            return self.visit(ctx.atom())

        # 3. Бинарные операции
        if ctx.op:
            left_type = self.visit(ctx.expression(0))
            right_type = self.visit(ctx.expression(1))
            op = ctx.op.type

            # Логические
            if op in [ListLangParser.AND, ListLangParser.OR]:
                return BOOL
                # if (left_type != BOOL and left_type != ELEMENT) or (right_type != BOOL and right_type != ELEMENT):
                #     print(f"Warning: Implicit cast to bool in logical operation [line {ctx.start.line}]")
                # return BOOL

            # Сравнения
            if op in [ListLangParser.EQUALS, ListLangParser.NOT_EQ,
                      ListLangParser.LESS_THAN, ListLangParser.GREATER_THAN,
                      ListLangParser.LT_EQ, ListLangParser.GT_EQ]:
                return BOOL

            # Арифметика
            if op in [ListLangParser.ADD, ListLangParser.MINUS,
                      ListLangParser.MULT, ListLangParser.DIV, ListLangParser.MOD]:
                if left_type == FLOAT or right_type == FLOAT:
                    return FLOAT
                if left_type == INT and right_type == INT:
                    return INT
                if op == ListLangParser.ADD and (left_type == STR or right_type == STR):
                    return STR
                # Если один из типов Element (неизвестен), допускаем операцию
                if left_type == ELEMENT or right_type == ELEMENT:
                    return ELEMENT

                raise SemanticError(f"Incompatible types for arithmetic: {left_type} and {right_type}", ctx)

        # Скобки ( expression )
        if len(ctx.expression()) == 1:
            return self.visit(ctx.expression(0))

        return ELEMENT

    def visitAtom(self, ctx: ListLangParser.AtomContext):
        # Литерал
        if ctx.literal():
            return get_literal_type(ctx.literal())

        name = ctx.NAME(0).getText()

        # Вызов функции: func(args) или obj.method(args)
        if ctx.OPEN_PAREN():
            # Это вызов функции или метода
            is_method = ctx.DOT() is not None

            # Если это метод obj.name(), то name - это obj
            if is_method:
                obj_name = name
                method_name = ctx.NAME(1).getText()

                # Проверка существования объекта
                obj_sym = self.current_scope.resolve(obj_name)
                if obj_sym is None:
                    raise SemanticError(f"Undefined object: '{obj_name}'", ctx)

                # Проверка методов для встроенных типов (List, Tree)
                if obj_sym.sym_type == LIST or obj_sym.sym_type == TREE:
                    # Разрешаем стандартные методы без глубокой проверки сигнатуры пока
                    valid_methods = ["add", "get", "len", "remove", "insert", "merge"]
                    if method_name not in valid_methods:
                        raise SemanticError(f"Unknown method '{method_name}' for type {obj_sym.sym_type}", ctx)

                    # Возвращаемые типы для методов
                    if method_name in ["len"]: return INT
                    if method_name in ["get"]: return ELEMENT
                    return VOID
                else:
                    # Вызов метода у неизвестного типа (dynamic)
                    return ELEMENT
            else:
                # Обычная функция
                func_sym = self.current_scope.resolve(name)
                if func_sym is None:
                    raise SemanticError(f"Undefined function: '{name}'", ctx)
                if func_sym.kind != "func":
                    raise SemanticError(f"'{name}' is not a function", ctx)

                # Проверка аргументов (количество)
                args_count = 0
                if ctx.arg_list():
                    args_count = len(ctx.arg_list().expression())

                # Проверка аргументов
                if func_sym.name != "write" and len(func_sym.params) != args_count:
                    raise SemanticError(f"Function '{name}' expects {len(func_sym.params)} arguments, got {args_count}",
                                        ctx)

                return func_sym.return_type if func_sym.return_type else VOID

        # Доступ к члену: obj.field
        elif ctx.DOT():
            # : Implement member access check
            return ELEMENT

        # Просто переменная
        else:
            sym = self.current_scope.resolve(name)
            if sym is None:
                raise SemanticError(f"Undefined variable: '{name}'", ctx)
            return sym.sym_type

    def visitFor_statement(self, ctx: ListLangParser.For_statementContext):
        # for a, b in list_expr: ...

        # 1. Вычисляем тип итерируемого объекта
        # Грамматика for: FOR target_list IN expression_list COLON suite
        # Обычно итерируется по одному выражению, но грамматика позволяет list.
        # Допустим, мы берем первое выражение.
        iterable_type = self.visit(ctx.expression_list().expression(0))

        if iterable_type not in [LIST, TREE, STR, ELEMENT]:
            raise SemanticError(f"For loop over non-iterable type: {iterable_type}", ctx)

        # 2. Создаем scope цикла
        self.enter_scope()

        # 3. Объявляем переменные цикла
        target_names = [t.getText() for t in ctx.target_list().NAME()]
        for name in target_names:
            # Тип переменной цикла зависит от содержимого списка. 
            # Т.к. дженериков полноценных нет, считаем ELEMENT
            self.current_scope.define(Symbol(name, ELEMENT, "var"))

        # 4. Тело
        self.visit(ctx.suite())

        self.leave_scope()

    def visitIf_statement(self, ctx: ListLangParser.If_statementContext):
        # IF expression COLON suite (ELSE ...)
        cond_type = self.visit(ctx.expression())
        if cond_type != BOOL and cond_type != ELEMENT:
            pass  # Warning implicit cast to bool

        self.enter_scope()
        self.visit(ctx.suite(0))  # Main block
        self.leave_scope()

        if ctx.ELSE():
            self.enter_scope()
            self.visit(ctx.suite(1))  # Else block
            self.leave_scope()

    def visitWhile_statement(self, ctx: ListLangParser.While_statementContext):
        cond_type = self.visit(ctx.expression())

        self.enter_scope()
        self.visit(ctx.suite())
        self.leave_scope()

    def visitSuite(self, ctx: ListLangParser.SuiteContext):
        # Suite просто содержит statement list
        return self.visitChildren(ctx)
