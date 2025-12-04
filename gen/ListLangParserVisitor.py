# Generated from F:/_uni/4_course/YAPIS/ListLangParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ListLangParser import ListLangParser
else:
    from ListLangParser import ListLangParser

# This class defines a complete generic visitor for a parse tree produced by ListLangParser.

class ListLangParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ListLangParser#program.
    def visitProgram(self, ctx:ListLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#simple_stmt.
    def visitSimple_stmt(self, ctx:ListLangParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:ListLangParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#target_list.
    def visitTarget_list(self, ctx:ListLangParser.Target_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#expression_stmt.
    def visitExpression_stmt(self, ctx:ListLangParser.Expression_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#return_stmt.
    def visitReturn_stmt(self, ctx:ListLangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#break_stmt.
    def visitBreak_stmt(self, ctx:ListLangParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#compound_statement.
    def visitCompound_statement(self, ctx:ListLangParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#suite.
    def visitSuite(self, ctx:ListLangParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#statement.
    def visitStatement(self, ctx:ListLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#stmt_list.
    def visitStmt_list(self, ctx:ListLangParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#func_decl.
    def visitFunc_decl(self, ctx:ListLangParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#parameter_list.
    def visitParameter_list(self, ctx:ListLangParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#param.
    def visitParam(self, ctx:ListLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#if_statement.
    def visitIf_statement(self, ctx:ListLangParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#while_statement.
    def visitWhile_statement(self, ctx:ListLangParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#for_statement.
    def visitFor_statement(self, ctx:ListLangParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#switch_statement.
    def visitSwitch_statement(self, ctx:ListLangParser.Switch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#case_block.
    def visitCase_block(self, ctx:ListLangParser.Case_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#default_block.
    def visitDefault_block(self, ctx:ListLangParser.Default_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#expression_list.
    def visitExpression_list(self, ctx:ListLangParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#expression.
    def visitExpression(self, ctx:ListLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#atom.
    def visitAtom(self, ctx:ListLangParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#arg_list.
    def visitArg_list(self, ctx:ListLangParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLangParser#literal.
    def visitLiteral(self, ctx:ListLangParser.LiteralContext):
        return self.visitChildren(ctx)



del ListLangParser