from compiler.ast_nodes import Program, Function, Parameter, Assignment, ReturnStatement, BreakStatement, IfStatement, \
    WhileStatement, ForStatement, SwitchStatement, CaseBlock, UnaryOp, BinaryOp, MethodCall, MemberAccess, FunctionCall, \
    Variable, Literal, Type
from gen.ListLangParser import ListLangParser
from gen.ListLangParserVisitor import ListLangParserVisitor


class ASTBuilder(ListLangParserVisitor):
    def __init__(self):
        self.errors = []

    def visitProgram(self, ctx: ListLangParser.ProgramContext):
        functions = []
        statements = []

        for stmt_ctx in ctx.statement():
            if stmt_ctx.compound_statement():
                compound = stmt_ctx.compound_statement()
                if compound.func_decl():
                    func = self.visit(compound.func_decl())
                    if func:
                        functions.append(func)
                else:
                    stmt = self.visit(compound)
                    if stmt:
                        statements.append(stmt)
            elif stmt_ctx.stmt_list():
                stmt_list = self.visit(stmt_ctx.stmt_list())
                if stmt_list:
                    statements.extend(stmt_list)
        return Program(functions=functions, statements=statements)

    def visitFunc_decl(self, ctx: ListLangParser.Func_declContext):
        name = ctx.NAME().getText()

        parameters = []
        if ctx.parameter_list():
            parameters = self.visit(ctx.parameter_list())

        body = self.visit(ctx.suite())

        return Function(name=name, parameters=parameters, body=body)

    def visitParameter_list(self, ctx: ListLangParser.Parameter_listContext):
        parameters = []
        for param_ctx in ctx.param():
            param = self.visit(param_ctx)
            parameters.append(param)
        return parameters

    def visitParam(self, ctx: ListLangParser.ParamContext):
        name = ctx.NAME().getText()
        by_reference = ctx.AMP() is not None
        return Parameter(name=name, by_reference=by_reference)

    def visitSuite(self, ctx: ListLangParser.SuiteContext):
        statements = []
        for stmt_ctx in ctx.statement():
            if stmt_ctx.compound_statement():
                stmt = self.visit(stmt_ctx.compound_statement())
                if stmt:
                    statements.append(stmt)
            elif stmt_ctx.stmt_list():
                stmt_list = self.visit(stmt_ctx.stmt_list())
                if stmt_list:
                    statements.extend(stmt_list)
        return statements

    def visitStmt_list(self, ctx: ListLangParser.Stmt_listContext):
        statements = []
        for simple_stmt_ctx in ctx.simple_stmt():
            stmt = self.visit(simple_stmt_ctx)
            if stmt:
                statements.append(stmt)
        return statements

    def visitSimple_stmt(self, ctx: ListLangParser.Simple_stmtContext):
        if ctx.assignment_stmt():
            return self.visit(ctx.assignment_stmt())
        elif ctx.expression_stmt():
            return self.visit(ctx.expression_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        return None

    def visitAssignment_stmt(self, ctx: ListLangParser.Assignment_stmtContext):
        targets = self.visit(ctx.target_list())
        values = self.visit(ctx.expression_list())
        return Assignment(targets=targets, values=values)

    def visitTarget_list(self, ctx: ListLangParser.Target_listContext):
        return [name.getText() for name in ctx.NAME()]

    def visitExpression_stmt(self, ctx: ListLangParser.Expression_stmtContext):
        return self.visit(ctx.expression())

    def visitReturn_stmt(self, ctx: ListLangParser.Return_stmtContext):
        values = self.visit(ctx.expression_list())
        return ReturnStatement(values=values)

    def visitBreak_stmt(self, ctx: ListLangParser.Break_stmtContext):
        return BreakStatement()

    def visitIf_statement(self, ctx: ListLangParser.If_statementContext):
        condition = self.visit(ctx.expression())
        then_body = self.visit(ctx.suite(0))
        else_body = []
        if ctx.ELSE():
            else_body = self.visit(ctx.suite(1))
        return IfStatement(condition=condition, then_body=then_body, else_body=else_body)

    def visitWhile_statement(self, ctx: ListLangParser.While_statementContext):
        condition = self.visit(ctx.expression())
        body = self.visit(ctx.suite())
        return WhileStatement(condition=condition, body=body)

    def visitFor_statement(self, ctx: ListLangParser.For_statementContext):
        targets = self.visit(ctx.target_list())
        iterables = self.visit(ctx.expression_list())
        body = self.visit(ctx.suite())
        return ForStatement(targets=targets, iterables=iterables, body=body)

    def visitSwitch_statement(self, ctx: ListLangParser.Switch_statementContext):
        expression = self.visit(ctx.expression())

        cases = []
        for case_ctx in ctx.case_block():
            case = self.visit(case_ctx)
            cases.append(case)

        default_case = None
        if ctx.default_block():
            default_case = self.visit(ctx.default_block())

        return SwitchStatement(expression=expression, cases=cases, default_case=default_case)

    def visitCase_block(self, ctx: ListLangParser.Case_blockContext):
        value = self.visit(ctx.expression())
        body = self.visit(ctx.suite())
        return CaseBlock(value=value, body=body)

    def visitDefault_block(self, ctx: ListLangParser.Default_blockContext):
        return self.visit(ctx.suite())

    def visitExpression_list(self, ctx: ListLangParser.Expression_listContext):
        expressions = []
        for expr_ctx in ctx.expression():
            expr = self.visit(expr_ctx)
            expressions.append(expr)
        return expressions

    def visitExpression(self, ctx: ListLangParser.ExpressionContext):
        # unary op NOT
        if ctx.NOT():
            operand = self.visit(ctx.expression(0))
            return UnaryOp(operator="!", operand=operand)

        # binary op
        if ctx.op:
            operator = ctx.op.text
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return BinaryOp(operator=operator, left=left, right=right)

        # Atom
        if ctx.atom():
            return self.visit(ctx.atom())

        return None

    def visitAtom(self, ctx: ListLangParser.AtomContext):
        if ctx.literal():
            return self.visit(ctx.literal())

        # expr in braces
        if ctx.OPEN_PAREN() and ctx.expression():
            return self.visit(ctx.expression())

        # method call
        if len(ctx.NAME()) == 2 and ctx.DOT() and ctx.OPEN_PAREN():
            object_name = ctx.NAME(0).getText()
            member_name = ctx.NAME(1).getText()
            arguments = []
            if ctx.arg_list():
                arguments = self.visit(ctx.arg_list())
            return MethodCall(object_name=object_name, method_name=member_name, arguments=arguments)

        # member access
        if len(ctx.NAME()) == 2 and ctx.DOT():
            object_name = ctx.NAME(0).getText()
            member_name = ctx.NAME(1).getText()
            return MemberAccess(object_name=object_name, member_name=member_name)

        # function call
        if len(ctx.NAME()) == 1 and ctx.OPEN_PAREN():
            name = ctx.NAME(0).getText()
            arguments = []
            if ctx.arg_list():
                arguments = self.visit(ctx.arg_list())
            return FunctionCall(name=name, arguments=arguments)

        # variable
        if len(ctx.NAME()) == 1:
            name = ctx.NAME(0).getText()
            return Variable(name=name)

        return None

    def visitArg_list(self, ctx: ListLangParser.Arg_listContext):
        arguments = []
        for expr_ctx in ctx.expression():
            arg = self.visit(expr_ctx)
            arguments.append(arg)
        return arguments

    def visitLiteral(self, ctx: ListLangParser.LiteralContext):
        if ctx.DECIMAL_INTEGER():
            value = int(ctx.DECIMAL_INTEGER().getText())
            return Literal(value=value, value_type=Type.INT)

        if ctx.FLOAT_NUMBER():
            text = ctx.FLOAT_NUMBER().getText()
            if text.endswith('.'):
                text += '0'
            elif text.startswith('.'):
                text = '0' + text
            value = float(text)
            return Literal(value=value, value_type=Type.FLOAT)

        if ctx.STRING():
            text = ctx.STRING().getText()
            # delete "
            value = text[1:-1]
            value = value.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
            return Literal(value=value, value_type=Type.STRING)

        if ctx.BOOLEAN():
            value = ctx.BOOLEAN().getText() == 'true'
            return Literal(value=value, value_type=Type.BOOL)

        # empty list
        if ctx.OPEN_BRACKET():
            return Literal(value=[], value_type=Type.LIST)

        return None
