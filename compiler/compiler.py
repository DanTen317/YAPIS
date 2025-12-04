import struct
from .ast_nodes import *


class SymbolTable:
    def __init__(self):
        self.scopes = [{}]
        self.locals_count = 0
        self.params_map = {}

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def declare(self, name, var_type, is_global=False, is_ref=False):
        scope = self.scopes[-1]
        if is_global:
            wasm_name = f"$global_{name}"
            scope[name] = (wasm_name, var_type, True, is_ref)
            return wasm_name
        else:
            wasm_name = f"$var_{name}_{self.locals_count}"
            self.locals_count += 1
            scope[name] = (wasm_name, var_type, False, is_ref)
            return wasm_name

    def register_param(self, name, var_type, index, is_ref=False):
        scope = self.scopes[-1]
        scope[name] = (index, var_type, False, is_ref)

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None


class WASMCompiler:
    def __init__(self):
        self.wat = []
        self.symbols = SymbolTable()
        self.strings = {}
        self.string_offset_counter = 0
        self.loop_stack = []
        self.func_locals = []
        self.current_func_return_type = Type.VOID
        self.last_expr_type = Type.UNKNOWN
        self.void_functions = set()
        self.for_loop_counter = 0

    def emit(self, line, indent=0):
        self.wat.append("  " * indent + line)

    def compile(self, program: Program):
        self.emit("(module")
        # Импорты
        self.emit('(import "env" "print_i32" (func $print_i32 (param i32)))', 1)
        self.emit('(import "env" "print_f32" (func $print_f32 (param f32)))', 1)
        self.emit('(import "env" "print_string" (func $print_string (param i32)))', 1)
        self.emit('(import "env" "read_i32" (func $read_i32 (result i32)))', 1)
        self.emit('(import "env" "print_char" (func $print_char (param i32)))', 1)
        self.emit('(import "env" "print_num" (func $print_num (param i32)))', 1)

        # Память
        self.emit('(memory $memory 1)', 1)
        self.emit('(export "memory" (memory $memory))', 1)
        self.emit('(global $heap_ptr (mut i32) (i32.const 1024))', 1)

        # Глобальные переменные
        self.emit('(global $temp_ptr (mut i32) (i32.const 0))', 1)
        self.emit('(global $temp_i32 (mut i32) (i32.const 0))', 1)
        self.emit('(global $temp_f32 (mut f32) (f32.const 0.0))', 1)

        self._collect_strings(program)
        self._emit_list_helpers()
        self._prescan_function_signatures(program.functions)

        for func in program.functions:
            self.visit_FUNCTION(func)

        self.emit('(func $main (export "main")', 1)
        self.symbols.enter_scope()

        self.for_loop_counter = 0
        self._scan_and_declare_locals(program.statements)
        self.for_loop_counter = 0

        for stmt in program.statements:
            self._visit_statement(stmt, indent=2)

        self.symbols.exit_scope()
        self.emit(')', 1)

        for s_val, offset in self.strings.items():
            escaped = s_val.replace('"', '\\"').replace('\n', '\\0A')
            self.emit(f'(data (i32.const {offset}) "{escaped}\\00")', 1)

        self.emit(")")
        return "\n".join(self.wat)

    # --- LIST HELPERS ---
    def _emit_list_helpers(self):
        indent = 1
        # $malloc
        self.emit('(func $malloc (param $size i32) (result i32)', indent)
        self.emit('  global.get $heap_ptr', indent)
        self.emit('  local.get $size', indent)
        self.emit('  global.get $heap_ptr', indent)
        self.emit('  i32.add', indent)
        self.emit('  global.set $heap_ptr', indent)
        self.emit(')', indent)

        # $list_new
        self.emit('(func $list_new (param $capacity i32) (result i32)', indent)
        self.emit('  (local $head i32) (local $data i32)', indent)
        self.emit('  i32.const 8', indent)
        self.emit('  call $malloc', indent)
        self.emit('  local.set $head', indent)
        self.emit('  local.get $capacity', indent)
        self.emit('  i32.const 4', indent)
        self.emit('  i32.mul', indent)
        self.emit('  call $malloc', indent)
        self.emit('  local.set $data', indent)
        self.emit('  local.get $head', indent)
        self.emit('  local.get $capacity', indent)
        self.emit('  i32.store', indent)
        self.emit('  local.get $head', indent)
        self.emit('  local.get $data', indent)
        self.emit('  i32.store offset=4', indent)
        self.emit('  local.get $head', indent)
        self.emit(')', indent)

        # $list_add_poly: Добавляет ячейку {type, value}
        self.emit('(func $list_add_poly (param $head i32) (param $type i32) (param $val i32)', indent)
        self.emit('  (local $old_size i32) (local $old_ptr i32) (local $new_ptr i32) (local $i i32) (local $cell i32)',
                  indent)

        # 1. Создаем ячейку (Cell)
        self.emit('  i32.const 8', indent)  # 8 байт: [type, value]
        self.emit('  call $malloc', indent)
        self.emit('  local.set $cell', indent)
        self.emit('  local.get $cell', indent)
        self.emit('  local.get $type', indent)
        self.emit('  i32.store', indent)  # Store Type at 0
        self.emit('  local.get $cell', indent)
        self.emit('  local.get $val', indent)
        self.emit('  i32.store offset=4', indent)  # Store Value at 4

        # 2. Реаллокация
        self.emit('  local.get $head', indent)
        self.emit('  i32.load', indent)
        self.emit('  local.set $old_size', indent)
        self.emit('  local.get $head', indent)
        self.emit('  i32.load offset=4', indent)
        self.emit('  local.set $old_ptr', indent)

        self.emit('  local.get $old_size', indent)
        self.emit('  i32.const 1', indent)
        self.emit('  i32.add', indent)
        self.emit('  i32.const 4', indent)
        self.emit('  i32.mul', indent)
        self.emit('  call $malloc', indent)
        self.emit('  local.set $new_ptr', indent)

        # Копирование
        self.emit('  (block $break (loop $loop', indent)
        self.emit('    local.get $i', indent)
        self.emit('    local.get $old_size', indent)
        self.emit('    i32.ge_s', indent)
        self.emit('    br_if $break', indent)
        self.emit('    local.get $new_ptr', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 4', indent)
        self.emit('    i32.mul', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.get $old_ptr', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 4', indent)
        self.emit('    i32.mul', indent)
        self.emit('    i32.add', indent)
        self.emit('    i32.load', indent)
        self.emit('    i32.store', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 1', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.set $i', indent)
        self.emit('    br $loop', indent)
        self.emit('  ))', indent)

        # Сохранение указателя на ячейку в новый массив
        self.emit('  local.get $new_ptr', indent)
        self.emit('  local.get $old_size', indent)
        self.emit('  i32.const 4', indent)
        self.emit('  i32.mul', indent)
        self.emit('  i32.add', indent)
        self.emit('  local.get $cell', indent)
        self.emit('  i32.store', indent)

        self.emit('  local.get $head', indent)
        self.emit('  local.get $new_ptr', indent)
        self.emit('  i32.store offset=4', indent)
        self.emit('  local.get $head', indent)
        self.emit('  local.get $old_size', indent)
        self.emit('  i32.const 1', indent)
        self.emit('  i32.add', indent)
        self.emit('  i32.store', indent)
        self.emit(')', indent)

        # $list_get
        self.emit('(func $list_get (param $head i32) (param $index i32) (result i32)', indent)
        self.emit('  (local $size i32)', indent)
        self.emit('  local.get $head', indent)
        self.emit('  i32.load', indent)
        self.emit('  local.set $size', indent)
        self.emit('  local.get $index', indent)
        self.emit('  local.get $size', indent)
        self.emit('  i32.ge_u', indent)
        self.emit('  if', indent)
        self.emit('    i32.const 0', indent)
        self.emit('    return', indent)
        self.emit('  end', indent)
        self.emit('  local.get $head', indent)
        self.emit('  i32.load offset=4', indent)
        self.emit('  local.get $index', indent)
        self.emit('  i32.const 4', indent)
        self.emit('  i32.mul', indent)
        self.emit('  i32.add', indent)
        self.emit('  i32.load', indent)  # Возвращаем Cell Ptr
        self.emit(')', indent)

        # $print_list
        self.emit('(func $print_list (param $head i32)', indent)
        self.emit('  (local $size i32) (local $ptr i32) (local $i i32) (local $cell i32) (local $type i32)', indent)
        self.emit('  local.get $head', indent)
        self.emit('  i32.load', indent)
        self.emit('  local.set $size', indent)
        self.emit('  local.get $head', indent)
        self.emit('  i32.load offset=4', indent)
        self.emit('  local.set $ptr', indent)

        self.emit('  i32.const 91', indent)
        self.emit('  call $print_char', indent)

        self.emit('  (block $break (loop $loop', indent)
        self.emit('    local.get $i', indent)
        self.emit('    local.get $size', indent)
        self.emit('    i32.ge_s', indent)
        self.emit('    br_if $break', indent)

        self.emit('    local.get $ptr', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 4', indent)
        self.emit('    i32.mul', indent)
        self.emit('    i32.add', indent)
        self.emit('    i32.load', indent)
        self.emit('    local.set $cell', indent)

        self.emit('    local.get $cell', indent)
        self.emit('    i32.load', indent)
        self.emit('    local.set $type', indent)

        # INT
        self.emit('    local.get $type', indent)
        self.emit('    i32.const 0', indent)
        self.emit('    i32.eq', indent)
        self.emit('    if', indent)
        self.emit('      local.get $cell', indent)
        self.emit('      i32.load offset=4', indent)
        self.emit('      call $print_num', indent)
        self.emit('    else', indent)

        # FLOAT
        self.emit('    local.get $type', indent)
        self.emit('    i32.const 1', indent)
        self.emit('    i32.eq', indent)
        self.emit('    if', indent)
        self.emit('      local.get $cell', indent)
        self.emit('      i32.load offset=4', indent)
        self.emit('      f32.reinterpret_i32', indent)
        self.emit('      call $print_f32', indent)
        self.emit('    else', indent)

        # STRING
        self.emit('    local.get $type', indent)
        self.emit('    i32.const 2', indent)
        self.emit('    i32.eq', indent)
        self.emit('    if', indent)
        self.emit('      local.get $cell', indent)
        self.emit('      i32.load offset=4', indent)
        self.emit('      call $print_string', indent)
        self.emit('    end', indent)
        self.emit('    end', indent)
        self.emit('    end', indent)

        self.emit('    local.get $i', indent)
        self.emit('    i32.const 1', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.get $size', indent)
        self.emit('    i32.lt_s', indent)
        self.emit('    if', indent)
        self.emit('      i32.const 44', indent)
        self.emit('      call $print_char', indent)
        self.emit('      i32.const 32', indent)
        self.emit('      call $print_char', indent)
        self.emit('    end', indent)

        self.emit('    local.get $i', indent)
        self.emit('    i32.const 1', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.set $i', indent)
        self.emit('    br $loop', indent)
        self.emit('  ))', indent)

        self.emit('  i32.const 93', indent)
        self.emit('  call $print_char', indent)
        self.emit('  i32.const 10', indent)
        self.emit('  call $print_char', indent)
        self.emit(')', indent)

        # $list_concat
        self.emit('(func $list_concat (param $h1 i32) (param $h2 i32) (result i32)', indent)
        self.emit(
            '  (local $s1 i32) (local $s2 i32) (local $total i32) (local $new_h i32) (local $i i32) (local $src i32) (local $dst i32)',
            indent)
        self.emit('  local.get $h1', indent)
        self.emit('  i32.load', indent)
        self.emit('  local.set $s1', indent)
        self.emit('  local.get $h2', indent)
        self.emit('  i32.load', indent)
        self.emit('  local.set $s2', indent)
        self.emit('  local.get $s1', indent)
        self.emit('  local.get $s2', indent)
        self.emit('  i32.add', indent)
        self.emit('  local.set $total', indent)
        self.emit('  local.get $total', indent)
        self.emit('  call $list_new', indent)
        self.emit('  local.set $new_h', indent)
        self.emit('  local.get $new_h', indent)
        self.emit('  i32.load offset=4', indent)
        self.emit('  local.set $dst', indent)
        self.emit('  local.get $h1', indent)
        self.emit('  i32.load offset=4', indent)
        self.emit('  local.set $src', indent)
        self.emit('  i32.const 0', indent)
        self.emit('  local.set $i', indent)
        self.emit('  (block $b1 (loop $l1', indent)
        self.emit('    local.get $i', indent)
        self.emit('    local.get $s1', indent)
        self.emit('    i32.ge_s', indent)
        self.emit('    br_if $b1', indent)
        self.emit('    local.get $dst', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 4', indent)
        self.emit('    i32.mul', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.get $src', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 4', indent)
        self.emit('    i32.mul', indent)
        self.emit('    i32.add', indent)
        self.emit('    i32.load', indent)
        self.emit('    i32.store', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 1', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.set $i', indent)
        self.emit('    br $l1', indent)
        self.emit('  ))', indent)
        self.emit('  local.get $h2', indent)
        self.emit('  i32.load offset=4', indent)
        self.emit('  local.set $src', indent)
        self.emit('  i32.const 0', indent)
        self.emit('  local.set $i', indent)
        self.emit('  (block $b2 (loop $l2', indent)
        self.emit('    local.get $i', indent)
        self.emit('    local.get $s2', indent)
        self.emit('    i32.ge_s', indent)
        self.emit('    br_if $b2', indent)
        self.emit('    local.get $dst', indent)
        self.emit('    local.get $s1', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.add', indent)
        self.emit('    i32.const 4', indent)
        self.emit('    i32.mul', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.get $src', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 4', indent)
        self.emit('    i32.mul', indent)
        self.emit('    i32.add', indent)
        self.emit('    i32.load', indent)
        self.emit('    i32.store', indent)
        self.emit('    local.get $i', indent)
        self.emit('    i32.const 1', indent)
        self.emit('    i32.add', indent)
        self.emit('    local.set $i', indent)
        self.emit('    br $l2', indent)
        self.emit('  ))', indent)
        self.emit('  local.get $new_h', indent)
        self.emit(')', indent)

        # $unbox_i32: Принимает указатель на ячейку, возвращает i32.
        # Если внутри float, обрезает его.
        self.emit('(func $unbox_i32 (param $ptr i32) (result i32)', indent)
        self.emit('  (local $type i32) (local $val i32)', indent)
        self.emit('  local.get $ptr', indent)
        self.emit('  i32.load', indent)  # type
        self.emit('  local.set $type', indent)
        self.emit('  local.get $ptr', indent)
        self.emit('  i32.load offset=4', indent)  # bits
        self.emit('  local.set $val', indent)

        # Если тип == 1 (FLOAT)
        self.emit('  local.get $type', indent)
        self.emit('  i32.const 1', indent)
        self.emit('  i32.eq', indent)
        self.emit('  if', indent)
        self.emit('    local.get $val', indent)
        self.emit('    f32.reinterpret_i32', indent)  # биты -> float
        self.emit('    i32.trunc_f32_s', indent)  # float -> int
        self.emit('    return', indent)
        self.emit('  end', indent)

        # Иначе (INT или STRING) возвращаем как есть
        self.emit('  local.get $val', indent)
        self.emit(')', indent)

        # $unbox_f32: Принимает указатель на ячейку, возвращает f32.
        # Если внутри int, конвертирует в float.
        self.emit('(func $unbox_f32 (param $ptr i32) (result f32)', indent)
        self.emit('  (local $type i32) (local $val i32)', indent)
        self.emit('  local.get $ptr', indent)
        self.emit('  i32.load', indent)
        self.emit('  local.set $type', indent)
        self.emit('  local.get $ptr', indent)
        self.emit('  i32.load offset=4', indent)
        self.emit('  local.set $val', indent)

        # Если тип == 0 (INT)
        self.emit('  local.get $type', indent)
        self.emit('  i32.const 0', indent)
        self.emit('  i32.eq', indent)
        self.emit('  if', indent)
        self.emit('    local.get $val', indent)
        self.emit('    f32.convert_i32_s', indent)  # int -> float
        self.emit('    return', indent)
        self.emit('  end', indent)

        # Иначе считаем что там биты float
        self.emit('  local.get $val', indent)
        self.emit('  f32.reinterpret_i32', indent)
        self.emit(')', indent)

    def _prescan_function_signatures(self, functions):
        self.void_functions.add('write')
        self.void_functions.add('print_i32')
        self.void_functions.add('print_f32')
        self.void_functions.add('print_string')
        self.void_functions.add('print_num')
        self.void_functions.add('print_char')
        self.void_functions.add('swap')
        for func in functions:
            mangled_name = f"{func.name}_{len(func.parameters)}"
            is_void = True
            if func.return_type != Type.VOID and func.return_type != Type.UNKNOWN:
                is_void = False
            elif self._has_return_value(func.body):
                is_void = False
            if is_void: self.void_functions.add(mangled_name)

    def _has_return_value(self, stmts):
        for stmt in stmts:
            if isinstance(stmt, ReturnStatement) and stmt.values: return True
            if isinstance(stmt, IfStatement):
                if self._has_return_value(stmt.then_body) or self._has_return_value(stmt.else_body): return True
            elif isinstance(stmt, (WhileStatement, ForStatement)):
                if self._has_return_value(stmt.body): return True
            elif isinstance(stmt, SwitchStatement):
                for case in stmt.cases:
                    if self._has_return_value(case.body): return True
                if stmt.default_case and self._has_return_value(stmt.default_case): return True
        return False

    def _visit_statement(self, stmt, indent):
        self.visit(stmt, indent)
        should_drop = False
        if isinstance(stmt, (Literal, Variable, BinaryOp, UnaryOp)):
            should_drop = True
        elif isinstance(stmt, FunctionCall):
            mangled_name = f"{stmt.name}_{len(stmt.arguments)}"
            if stmt.name != 'write' and stmt.name != 'swap' and mangled_name not in self.void_functions:
                should_drop = True
        elif isinstance(stmt, MethodCall):
            if stmt.method_name == 'get' or stmt.method_name == 'len': should_drop = True
        if should_drop: self.emit('drop', indent)

    def _scan_and_declare_locals(self, stmts):
        if not stmts: return
        for stmt in stmts:
            if isinstance(stmt, Assignment):
                rhs_node = stmt.values[0] if stmt.values else None
                guessed_type = self._infer_type(rhs_node)
                for target_name in stmt.targets:
                    if not self.symbols.lookup(target_name):
                        wasm_type = 'f32' if guessed_type == Type.FLOAT else 'i32'
                        self.symbols.declare(target_name, guessed_type)
                        self.emit(f'(local $var_{target_name}_{self.symbols.locals_count - 1} {wasm_type})', 2)
            elif isinstance(stmt, IfStatement):
                self._scan_and_declare_locals(stmt.then_body)
                self._scan_and_declare_locals(stmt.else_body)
            elif isinstance(stmt, WhileStatement):
                self._scan_and_declare_locals(stmt.body)
            elif isinstance(stmt, ForStatement):
                loop_id = self.for_loop_counter
                self.for_loop_counter += 1
                self.emit(f'(local $for_idx_{loop_id} i32)', 2)
                self.emit(f'(local $for_len_{loop_id} i32)', 2)
                self.emit(f'(local $for_ptr_{loop_id} i32)', 2)
                for target_name in stmt.targets:
                    if not self.symbols.lookup(target_name):
                        self.symbols.declare(target_name, Type.ELEMENT)
                        self.emit(f'(local $var_{target_name}_{self.symbols.locals_count - 1} i32)', 2)
                self._scan_and_declare_locals(stmt.body)
            elif isinstance(stmt, SwitchStatement):
                for case in stmt.cases: self._scan_and_declare_locals(case.body)
                if stmt.default_case: self._scan_and_declare_locals(stmt.default_case)

    def _infer_type(self, node):
        if node is None: return Type.INT
        if isinstance(node, Literal): return node.type
        if isinstance(node, Variable):
            info = self.symbols.lookup(node.name)
            return info[1] if info else Type.INT
        if isinstance(node, BinaryOp):
            l = self._infer_type(node.left)
            r = self._infer_type(node.right)
            if l == Type.LIST or r == Type.LIST: return Type.LIST
            if l == Type.FLOAT or r == Type.FLOAT: return Type.FLOAT
            if node.operator in ['==', '!=', '<', '>', '<=', '>=']: return Type.BOOL
            return Type.INT

        # --- Обработка вызовов методов ---
        if isinstance(node, MethodCall):
            if node.method_name == 'get':
                return Type.ELEMENT
            if node.method_name == 'len':
                return Type.INT
            # add и другие void методы можно считать INT или VOID
            return Type.INT

        # Обработка вызовов функций (на будущее)
        if isinstance(node, FunctionCall):
            return Type.INT

        return Type.INT

    def _collect_strings(self, node):
        if isinstance(node, Literal) and node.type == Type.STRING:
            if node.value not in self.strings:
                self.strings[node.value] = self.string_offset_counter
                self.string_offset_counter += len(node.value.encode('utf-8')) + 1
        elif hasattr(node, '__dict__'):
            for key, value in node.__dict__.items():
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, ASTNode): self._collect_strings(item)
                elif isinstance(value, ASTNode):
                    self._collect_strings(value)

    def visit(self, node: ASTNode, indent=0):
        method_name = f'visit_{node.node_type.name}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node, indent)

    def generic_visit(self, node, indent):
        print(f"Warning: No visitor for {node.node_type}")
        return None

    def visit_FUNCTION(self, node: Function, indent=1):
        self.symbols.locals_count = 0
        self.for_loop_counter = 0
        self.symbols.enter_scope()
        params_str = ""
        for i, param in enumerate(node.parameters):
            p_type = "i32"
            if param.type == Type.FLOAT: p_type = "f32"
            params_str += f" (param $p_{param.name} {p_type})"
            self.symbols.register_param(param.name, param.type, f"$p_{param.name}", param.by_reference)
        mangled_name = f"{node.name}_{len(node.parameters)}"
        result_str = ""
        is_void = mangled_name in self.void_functions
        if not is_void:
            r_type = "f32" if node.return_type == Type.FLOAT else "i32"
            result_str = f" (result {r_type})"
            self.current_func_return_type = Type.INT if r_type == 'i32' else Type.FLOAT
        else:
            self.current_func_return_type = Type.VOID
        self.emit(f'(func ${mangled_name}{params_str}{result_str}', indent)
        self.for_loop_counter = 0
        self._scan_and_declare_locals(node.body)
        self.for_loop_counter = 0
        for stmt in node.body: self._visit_statement(stmt, indent + 1)
        if not is_void and not isinstance(node.body[-1], ReturnStatement):
            if "f32" in result_str:
                self.emit('f32.const 0.0', indent + 1)
            else:
                self.emit('i32.const 0', indent + 1)
        self.emit(')', indent)
        self.symbols.exit_scope()

    def visit_ASSIGNMENT(self, node: Assignment, indent):
        for val in node.values: self.visit(val, indent)
        for target_name in reversed(node.targets):
            info = self.symbols.lookup(target_name)
            if not info:
                self.emit('drop', indent)
                continue
            wasm_name, v_type, is_global, is_ref = info
            if v_type == Type.INT and self.last_expr_type == Type.FLOAT:
                self.emit('i32.trunc_f32_s', indent)
            elif v_type == Type.FLOAT and self.last_expr_type == Type.INT:
                self.emit('f32.convert_i32_s', indent)

            # if is_ref:
            #     if v_type == Type.FLOAT:
            #         self.emit('global.set $temp_f32', indent)
            #         self.emit(f'local.get {wasm_name}', indent)
            #         self.emit('global.get $temp_f32', indent)
            #         self.emit('f32.store', indent)
            #     else:
            #         self.emit('global.set $temp_i32', indent)
            #         self.emit(f'local.get {wasm_name}', indent)
            #         self.emit('global.get $temp_i32', indent)
            #         self.emit('i32.store', indent)
            elif is_global:
                self.emit(f'global.set {wasm_name}', indent)
            else:
                self.emit(f'local.set {wasm_name}', indent)

    def visit_LITERAL(self, node: Literal, indent):
        self.last_expr_type = node.type
        if node.type == Type.INT:
            self.emit(f'i32.const {node.value}', indent)
        elif node.type == Type.FLOAT:
            self.emit(f'f32.const {node.value}', indent)
        elif node.type == Type.BOOL:
            self.emit(f'i32.const {1 if node.value else 0}', indent)
        elif node.type == Type.STRING:
            self.emit(f'i32.const {self.strings.get(node.value, 0)}', indent)
        elif node.type == Type.LIST:
            count = len(node.value)
            self.emit(f'i32.const {count}', indent)
            self.emit(f'call $list_new', indent)
            self.emit('global.set $temp_ptr', indent)
            for item in node.value:
                self.emit('global.get $temp_ptr', indent)
                type_code = 0
                if item.type == Type.FLOAT:
                    type_code = 1
                elif item.type == Type.STRING:
                    type_code = 2
                self.emit(f'i32.const {type_code}', indent)
                self.visit(item, indent)
                if item.type == Type.FLOAT: self.emit('i32.reinterpret_f32', indent)
                self.emit('call $list_add_poly', indent)
            self.emit('global.get $temp_ptr', indent)

    def visit_VARIABLE(self, node: Variable, indent):
        info = self.symbols.lookup(node.name)
        if not info:
            self.emit('i32.const 0', indent)
            self.last_expr_type = Type.INT
            return
        wasm_name, v_type, is_global, is_ref = info
        self.last_expr_type = v_type
        # if is_ref:
        #     self.emit(f'local.get {wasm_name}', indent)
        #     self.emit('f32.load' if v_type == Type.FLOAT else 'i32.load', indent)
        # el
        if is_global:
            self.emit(f'global.get {wasm_name}', indent)
        else:
            self.emit(f'local.get {wasm_name}', indent)

    def visit_BINARY_OP(self, node: BinaryOp, indent):
        left_type = self._infer_type(node.left)
        right_type = self._infer_type(node.right)

        def unbox_if_needed(val_type, target_is_float):
            if val_type == Type.ELEMENT:
                # Если ожидаем float (потому что второй операнд float),
                # вызываем $unbox_f32
                if target_is_float:
                    self.emit('call $unbox_f32', indent)
                else:
                    # Иначе приводим к int (даже если там float)
                    self.emit('call $unbox_i32', indent)
            elif val_type == Type.INT and target_is_float:
                self.emit('f32.convert_i32_s', indent)

        if left_type == Type.LIST or right_type == Type.LIST:
            self.visit(node.left, indent)
            self.visit(node.right, indent)
            if node.operator == '+':
                self.emit('call $list_concat', indent)
                self.last_expr_type = Type.LIST
            return

        is_float_op = (left_type == Type.FLOAT or right_type == Type.FLOAT)
        self.visit(node.left, indent)
        unbox_if_needed(left_type, is_float_op)
        self.visit(node.right, indent)
        unbox_if_needed(right_type, is_float_op)
        op_code = self._get_binary_opcode(node.operator, is_float_op)
        self.emit(op_code, indent)
        self.last_expr_type = Type.FLOAT if is_float_op else Type.INT

    def _get_binary_opcode(self, op, is_float):
        if is_float:
            if op == '+': return 'f32.add'
            if op == '-': return 'f32.sub'
            if op == '*': return 'f32.mul'
            if op == '/': return 'f32.div'
            if op == '<': return 'f32.lt'
            if op == '>': return 'f32.gt'
            if op == '==': return 'f32.eq'
            if op == '!=': return 'f32.ne'
            return 'f32.add'
        else:
            if op == '+': return 'i32.add'
            if op == '-': return 'i32.sub'
            if op == '*': return 'i32.mul'
            if op == '/': return 'i32.div_s'
            if op == '%': return 'i32.rem_s'
            if op == '==': return 'i32.eq'
            if op == '!=': return 'i32.ne'
            if op == '<': return 'i32.lt_s'
            if op == '>': return 'i32.gt_s'
            if op == '&&': return 'i32.and'
            if op == '||': return 'i32.or'
            return 'i32.add'

    def visit_UNARY_OP(self, node: UnaryOp, indent):
        self.visit(node.operand, indent)
        if node.operator == '!': self.emit('i32.eqz', indent)

    def visit_IF_STATEMENT(self, node: IfStatement, indent):
        self.visit(node.condition, indent)
        self.emit('if', indent)
        for stmt in node.then_body: self._visit_statement(stmt, indent + 1)
        if node.else_body:
            self.emit('else', indent)
            for stmt in node.else_body: self._visit_statement(stmt, indent + 1)
        self.emit('end', indent)

    def visit_WHILE_STATEMENT(self, node: WhileStatement, indent):
        break_label = f"$break_{len(self.loop_stack)}"
        cont_label = f"$continue_{len(self.loop_stack)}"
        self.loop_stack.append((break_label, cont_label))
        self.emit(f'block {break_label}', indent)
        self.emit(f'loop {cont_label}', indent + 1)
        self.visit(node.condition, indent + 2)
        self.emit('i32.eqz', indent + 2)
        self.emit(f'br_if {break_label}', indent + 2)
        for stmt in node.body: self._visit_statement(stmt, indent + 2)
        self.emit(f'br {cont_label}', indent + 2)
        self.emit('end', indent + 1)
        self.emit('end', indent)
        self.loop_stack.pop()

    def visit_FOR_STATEMENT(self, node: ForStatement, indent):
        loop_id = self.for_loop_counter
        self.for_loop_counter += 1
        idx_var = f"$for_idx_{loop_id}"
        len_var = f"$for_len_{loop_id}"
        ptr_var = f"$for_ptr_{loop_id}"
        self.visit(node.iterables[0], indent)
        self.emit(f'local.set {ptr_var}', indent)
        self.emit(f'local.get {ptr_var}', indent)
        self.emit('i32.load', indent)
        self.emit(f'local.set {len_var}', indent)
        self.emit(f'local.get {ptr_var}', indent)
        self.emit('i32.load offset=4', indent)
        self.emit(f'local.set {ptr_var}', indent)
        self.emit('i32.const 0', indent)
        self.emit(f'local.set {idx_var}', indent)
        break_label = f"$break_for_{loop_id}"
        cont_label = f"$cont_for_{loop_id}"
        self.loop_stack.append((break_label, cont_label))
        self.emit(f'block {break_label}', indent)
        self.emit(f'loop {cont_label}', indent + 1)
        self.emit(f'local.get {idx_var}', indent + 2)
        self.emit(f'local.get {len_var}', indent + 2)
        self.emit('i32.ge_s', indent + 2)
        self.emit(f'br_if {break_label}', indent + 2)
        target_name = node.targets[0]
        info = self.symbols.lookup(target_name)
        if info:
            user_var = info[0]
            self.emit(f'local.get {ptr_var}', indent + 2)
            self.emit(f'local.get {idx_var}', indent + 2)
            self.emit('i32.const 4', indent + 2)
            self.emit('i32.mul', indent + 2)
            self.emit('i32.add', indent + 2)
            self.emit('i32.load', indent + 2)
            self.emit(f'local.set {user_var}', indent + 2)
        for stmt in node.body: self._visit_statement(stmt, indent + 2)
        self.emit(f'local.get {idx_var}', indent + 2)
        self.emit('i32.const 1', indent + 2)
        self.emit('i32.add', indent + 2)
        self.emit(f'local.set {idx_var}', indent + 2)
        self.emit(f'br {cont_label}', indent + 2)
        self.emit('end', indent + 1)
        self.emit('end', indent)
        self.loop_stack.pop()

    def visit_BREAK_STATEMENT(self, node: BreakStatement, indent):
        if self.loop_stack: self.emit(f'br {self.loop_stack[-1][0]}', indent)

    def visit_RETURN_STATEMENT(self, node: ReturnStatement, indent):
        if node.values:
            if isinstance(node.values, list) and len(node.values) > 0:
                self.visit(node.values[0], indent)
            else:
                self.visit(node.values, indent)
            if self.current_func_return_type == Type.INT and self.last_expr_type == Type.FLOAT:
                self.emit('i32.trunc_f32_s', indent)
            elif self.current_func_return_type == Type.FLOAT and self.last_expr_type == Type.INT:
                self.emit('f32.convert_i32_s', indent)
        self.emit('return', indent)

    def visit_CALL(self, node: FunctionCall, indent):
        if node.name == 'write':
            for arg in node.arguments:
                target_type = self._infer_type(arg)
                self.visit(arg, indent)
                if target_type == Type.LIST:
                    self.emit('call $print_list', indent)
                elif target_type == Type.STRING:
                    self.emit('call $print_string', indent)
                elif target_type == Type.FLOAT:
                    self.emit('call $print_f32', indent)
                elif target_type == Type.ELEMENT:
                    self.emit('i32.load offset=4', indent)  # Unbox for printing
                    self.emit('call $print_i32', indent)
                else:
                    self.emit('call $print_i32', indent)
            return
        if node.name == 'read':
            self.emit('call $read_i32', indent)
            return
        if node.name == 'swap':
            arg1 = node.arguments[0]
            arg2 = node.arguments[1]
            info1 = self.symbols.lookup(arg1.name)
            info2 = self.symbols.lookup(arg2.name)
            if not info1 or not info2: return
            name1, type1, is_global1, _ = info1
            name2, _, is_global2, _ = info2
            if is_global1:
                self.emit(f'global.get {name1}', indent)
            else:
                self.emit(f'local.get {name1}', indent)
            if is_global2:
                self.emit(f'global.get {name2}', indent)
            else:
                self.emit(f'local.get {name2}', indent)
            if is_global1:
                self.emit(f'global.set {name1}', indent)
            else:
                self.emit(f'local.set {name1}', indent)
            if is_global2:
                self.emit(f'global.set {name2}', indent)
            else:
                self.emit(f'local.set {name2}', indent)
            return
        mangled_name = f"{node.name}_{len(node.arguments)}"
        for arg in node.arguments:
            arg_type = self._infer_type(arg)
            self.visit(arg, indent)

            # Если передаем ELEMENT, нужно его распаковать.
            # Так как мы не знаем сигнатуру функции (принимает она float или int),
            # для упрощения приводим к i32 (стандартное поведение для нашего компилятора)
            if arg_type == Type.ELEMENT:
                self.emit('call $unbox_i32', indent)
        self.emit(f'call ${mangled_name}', indent)


    def visit_SWITCH_STATEMENT(self, node: SwitchStatement, indent):
        temp_var = self.symbols.declare(f"switch_temp_{len(self.loop_stack)}", Type.INT)
        self.emit(f'(local {temp_var} i32)', indent)
        self.visit(node.expression, indent)
        self.emit(f'local.set {temp_var}', indent)

        def build_cases(cases, index):
            if index >= len(cases):
                if node.default_case:
                    for stmt in node.default_case: self._visit_statement(stmt, indent + 1)
                return
            case = cases[index]
            self.emit(f'local.get {temp_var}', indent)
            self.visit(case.value, indent)
            self.emit('i32.eq', indent)
            self.emit('if', indent)
            for stmt in case.body: self._visit_statement(stmt, indent + 1)
            self.emit('else', indent)
            build_cases(cases, index + 1)
            self.emit('end', indent)

        build_cases(node.cases, 0)

    def visit_METHOD_CALL(self, node: MethodCall, indent):
        if node.method_name == "add":
            info = self.symbols.lookup(node.object_name)
            if not info: return
            var_name, _, _, _ = info
            self.emit(f'local.get {var_name}', indent)
            arg_node = node.arguments[0]
            arg_type = self._infer_type(arg_node)
            type_code = 0
            if arg_type == Type.FLOAT:
                type_code = 1
            elif arg_type == Type.STRING:
                type_code = 2
            self.emit(f'i32.const {type_code}', indent)
            self.visit(arg_node, indent)
            if arg_type == Type.FLOAT: self.emit('i32.reinterpret_f32', indent)
            self.emit('call $list_add_poly', indent)
            self.last_expr_type = Type.VOID
        elif node.method_name == "len":
            info = self.symbols.lookup(node.object_name)
            if not info: return
            var_name, _, _, _ = info
            self.emit(f'local.get {var_name}', indent)
            self.emit('i32.load', indent)
            self.last_expr_type = Type.INT
        elif node.method_name == "get":
            info = self.symbols.lookup(node.object_name)
            if not info: return
            var_name, _, _, _ = info
            self.emit(f'local.get {var_name}', indent)
            if len(node.arguments) > 0:
                self.visit(node.arguments[0], indent)
            else:
                self.emit('i32.const 0', indent)
            self.emit('call $list_get', indent)
            self.last_expr_type = Type.ELEMENT
        else:
            print(f"Unknown method {node.method_name}")