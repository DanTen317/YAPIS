# Generated from F:/_uni/4_course/YAPIS/ListLangParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,276,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,5,0,59,8,0,10,0,12,0,62,9,0,5,0,64,8,0,10,0,
        12,0,67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,75,8,1,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,5,3,84,8,3,10,3,12,3,87,9,3,1,4,1,4,1,5,1,5,1,5,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,3,7,101,8,7,1,8,1,8,1,8,1,8,4,8,107,8,8,11,
        8,12,8,108,1,8,1,8,4,8,113,8,8,11,8,12,8,114,1,8,1,8,3,8,119,8,8,
        1,9,1,9,1,9,1,9,1,9,3,9,126,8,9,1,10,1,10,1,10,5,10,131,8,10,10,
        10,12,10,134,9,10,1,11,1,11,1,11,1,11,3,11,140,8,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,5,12,149,8,12,10,12,12,12,152,9,12,1,13,3,
        13,155,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,166,
        8,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,4,17,186,8,17,11,17,12,17,187,1,17,
        3,17,191,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,
        1,19,1,20,1,20,1,20,5,20,207,8,20,10,20,12,20,210,9,20,1,21,1,21,
        1,21,1,21,3,21,216,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,5,21,230,8,21,10,21,12,21,233,9,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,245,8,22,1,22,1,22,
        1,22,1,22,3,22,251,8,22,1,22,1,22,1,22,1,22,1,22,3,22,258,8,22,1,
        23,1,23,1,23,5,23,263,8,23,10,23,12,23,266,9,23,1,24,1,24,1,24,1,
        24,1,24,1,24,3,24,274,8,24,1,24,0,1,42,25,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,4,1,0,16,18,1,
        0,14,15,1,0,7,12,1,0,3,4,291,0,53,1,0,0,0,2,74,1,0,0,0,4,76,1,0,
        0,0,6,80,1,0,0,0,8,88,1,0,0,0,10,90,1,0,0,0,12,93,1,0,0,0,14,100,
        1,0,0,0,16,118,1,0,0,0,18,125,1,0,0,0,20,127,1,0,0,0,22,135,1,0,
        0,0,24,145,1,0,0,0,26,154,1,0,0,0,28,158,1,0,0,0,30,167,1,0,0,0,
        32,172,1,0,0,0,34,179,1,0,0,0,36,194,1,0,0,0,38,199,1,0,0,0,40,203,
        1,0,0,0,42,215,1,0,0,0,44,257,1,0,0,0,46,259,1,0,0,0,48,273,1,0,
        0,0,50,52,5,46,0,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,
        54,1,0,0,0,54,65,1,0,0,0,55,53,1,0,0,0,56,60,3,18,9,0,57,59,5,46,
        0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,64,
        1,0,0,0,62,60,1,0,0,0,63,56,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,1,69,1,1,0,
        0,0,70,75,3,8,4,0,71,75,3,4,2,0,72,75,3,10,5,0,73,75,3,12,6,0,74,
        70,1,0,0,0,74,71,1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,0,75,3,1,0,0,
        0,76,77,3,6,3,0,77,78,5,13,0,0,78,79,3,40,20,0,79,5,1,0,0,0,80,85,
        5,44,0,0,81,82,5,20,0,0,82,84,5,44,0,0,83,81,1,0,0,0,84,87,1,0,0,
        0,85,83,1,0,0,0,85,86,1,0,0,0,86,7,1,0,0,0,87,85,1,0,0,0,88,89,3,
        42,21,0,89,9,1,0,0,0,90,91,5,30,0,0,91,92,3,40,20,0,92,11,1,0,0,
        0,93,94,5,39,0,0,94,13,1,0,0,0,95,101,3,22,11,0,96,101,3,28,14,0,
        97,101,3,30,15,0,98,101,3,32,16,0,99,101,3,34,17,0,100,95,1,0,0,
        0,100,96,1,0,0,0,100,97,1,0,0,0,100,98,1,0,0,0,100,99,1,0,0,0,101,
        15,1,0,0,0,102,103,3,18,9,0,103,104,5,46,0,0,104,119,1,0,0,0,105,
        107,5,46,0,0,106,105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,
        109,1,0,0,0,109,110,1,0,0,0,110,112,5,1,0,0,111,113,3,18,9,0,112,
        111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,
        116,1,0,0,0,116,117,5,2,0,0,117,119,1,0,0,0,118,102,1,0,0,0,118,
        106,1,0,0,0,119,17,1,0,0,0,120,121,3,20,10,0,121,122,5,46,0,0,122,
        126,1,0,0,0,123,126,3,14,7,0,124,126,5,46,0,0,125,120,1,0,0,0,125,
        123,1,0,0,0,125,124,1,0,0,0,126,19,1,0,0,0,127,132,3,2,1,0,128,129,
        5,22,0,0,129,131,3,2,1,0,130,128,1,0,0,0,131,134,1,0,0,0,132,130,
        1,0,0,0,132,133,1,0,0,0,133,21,1,0,0,0,134,132,1,0,0,0,135,136,5,
        29,0,0,136,137,5,44,0,0,137,139,5,23,0,0,138,140,3,24,12,0,139,138,
        1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,5,24,0,0,142,143,
        5,21,0,0,143,144,3,16,8,0,144,23,1,0,0,0,145,150,3,26,13,0,146,147,
        5,20,0,0,147,149,3,26,13,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,
        1,0,0,0,150,151,1,0,0,0,151,25,1,0,0,0,152,150,1,0,0,0,153,155,5,
        6,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,157,5,
        44,0,0,157,27,1,0,0,0,158,159,5,31,0,0,159,160,3,42,21,0,160,161,
        5,21,0,0,161,165,3,16,8,0,162,163,5,32,0,0,163,164,5,21,0,0,164,
        166,3,16,8,0,165,162,1,0,0,0,165,166,1,0,0,0,166,29,1,0,0,0,167,
        168,5,35,0,0,168,169,3,42,21,0,169,170,5,21,0,0,170,171,3,16,8,0,
        171,31,1,0,0,0,172,173,5,36,0,0,173,174,3,6,3,0,174,175,5,37,0,0,
        175,176,3,40,20,0,176,177,5,21,0,0,177,178,3,16,8,0,178,33,1,0,0,
        0,179,180,5,33,0,0,180,181,3,42,21,0,181,182,5,21,0,0,182,183,5,
        46,0,0,183,185,5,1,0,0,184,186,3,36,18,0,185,184,1,0,0,0,186,187,
        1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,191,
        3,38,19,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,
        5,2,0,0,193,35,1,0,0,0,194,195,5,34,0,0,195,196,3,42,21,0,196,197,
        5,21,0,0,197,198,3,16,8,0,198,37,1,0,0,0,199,200,5,38,0,0,200,201,
        5,21,0,0,201,202,3,16,8,0,202,39,1,0,0,0,203,208,3,42,21,0,204,205,
        5,20,0,0,205,207,3,42,21,0,206,204,1,0,0,0,207,210,1,0,0,0,208,206,
        1,0,0,0,208,209,1,0,0,0,209,41,1,0,0,0,210,208,1,0,0,0,211,212,6,
        21,-1,0,212,213,5,5,0,0,213,216,3,42,21,2,214,216,3,44,22,0,215,
        211,1,0,0,0,215,214,1,0,0,0,216,231,1,0,0,0,217,218,10,6,0,0,218,
        219,7,0,0,0,219,230,3,42,21,7,220,221,10,5,0,0,221,222,7,1,0,0,222,
        230,3,42,21,6,223,224,10,4,0,0,224,225,7,2,0,0,225,230,3,42,21,5,
        226,227,10,3,0,0,227,228,7,3,0,0,228,230,3,42,21,4,229,217,1,0,0,
        0,229,220,1,0,0,0,229,223,1,0,0,0,229,226,1,0,0,0,230,233,1,0,0,
        0,231,229,1,0,0,0,231,232,1,0,0,0,232,43,1,0,0,0,233,231,1,0,0,0,
        234,258,3,48,24,0,235,258,5,44,0,0,236,237,5,44,0,0,237,238,5,19,
        0,0,238,258,5,44,0,0,239,240,5,44,0,0,240,241,5,19,0,0,241,242,5,
        44,0,0,242,244,5,23,0,0,243,245,3,46,23,0,244,243,1,0,0,0,244,245,
        1,0,0,0,245,246,1,0,0,0,246,258,5,24,0,0,247,248,5,44,0,0,248,250,
        5,23,0,0,249,251,3,46,23,0,250,249,1,0,0,0,250,251,1,0,0,0,251,252,
        1,0,0,0,252,258,5,24,0,0,253,254,5,23,0,0,254,255,3,42,21,0,255,
        256,5,24,0,0,256,258,1,0,0,0,257,234,1,0,0,0,257,235,1,0,0,0,257,
        236,1,0,0,0,257,239,1,0,0,0,257,247,1,0,0,0,257,253,1,0,0,0,258,
        45,1,0,0,0,259,264,3,42,21,0,260,261,5,20,0,0,261,263,3,42,21,0,
        262,260,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,
        265,47,1,0,0,0,266,264,1,0,0,0,267,274,5,42,0,0,268,274,5,41,0,0,
        269,274,5,43,0,0,270,274,5,40,0,0,271,272,5,27,0,0,272,274,5,28,
        0,0,273,267,1,0,0,0,273,268,1,0,0,0,273,269,1,0,0,0,273,270,1,0,
        0,0,273,271,1,0,0,0,274,49,1,0,0,0,26,53,60,65,74,85,100,108,114,
        118,125,132,139,150,154,165,187,190,208,215,229,231,244,250,257,
        264,273
    ]

class ListLangParser ( Parser ):

    grammarFileName = "ListLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'&&'", "'||'", 
                     "'!'", "'&'", "'<'", "'>'", "'=='", "'<='", "'>='", 
                     "'!='", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'.'", 
                     "','", "':'", "';'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'func'", "'return'", "'if'", "'else'", "'switch'", 
                     "'case'", "'while'", "'for'", "'in'", "'default'", 
                     "'break'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "AND", "OR", "NOT", 
                      "AMP", "LESS_THAN", "GREATER_THAN", "EQUALS", "LT_EQ", 
                      "GT_EQ", "NOT_EQ", "ASSIGNMENT", "ADD", "MINUS", "MULT", 
                      "DIV", "MOD", "DOT", "COMMA", "COLON", "SEMI_COLON", 
                      "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "FUNC", "RETURN", 
                      "IF", "ELSE", "SWITCH", "CASE", "WHILE", "FOR", "IN", 
                      "DEFAULT", "BREAK", "BOOLEAN", "FLOAT_NUMBER", "DECIMAL_INTEGER", 
                      "STRING", "NAME", "COMMENT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_simple_stmt = 1
    RULE_assignment_stmt = 2
    RULE_target_list = 3
    RULE_expression_stmt = 4
    RULE_return_stmt = 5
    RULE_break_stmt = 6
    RULE_compound_statement = 7
    RULE_suite = 8
    RULE_statement = 9
    RULE_stmt_list = 10
    RULE_func_decl = 11
    RULE_parameter_list = 12
    RULE_param = 13
    RULE_if_statement = 14
    RULE_while_statement = 15
    RULE_for_statement = 16
    RULE_switch_statement = 17
    RULE_case_block = 18
    RULE_default_block = 19
    RULE_expression_list = 20
    RULE_expression = 21
    RULE_atom = 22
    RULE_arg_list = 23
    RULE_literal = 24

    ruleNames =  [ "program", "simple_stmt", "assignment_stmt", "target_list", 
                   "expression_stmt", "return_stmt", "break_stmt", "compound_statement", 
                   "suite", "statement", "stmt_list", "func_decl", "parameter_list", 
                   "param", "if_statement", "while_statement", "for_statement", 
                   "switch_statement", "case_block", "default_block", "expression_list", 
                   "expression", "atom", "arg_list", "literal" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    AND=3
    OR=4
    NOT=5
    AMP=6
    LESS_THAN=7
    GREATER_THAN=8
    EQUALS=9
    LT_EQ=10
    GT_EQ=11
    NOT_EQ=12
    ASSIGNMENT=13
    ADD=14
    MINUS=15
    MULT=16
    DIV=17
    MOD=18
    DOT=19
    COMMA=20
    COLON=21
    SEMI_COLON=22
    OPEN_PAREN=23
    CLOSE_PAREN=24
    OPEN_BRACE=25
    CLOSE_BRACE=26
    OPEN_BRACKET=27
    CLOSE_BRACKET=28
    FUNC=29
    RETURN=30
    IF=31
    ELSE=32
    SWITCH=33
    CASE=34
    WHILE=35
    FOR=36
    IN=37
    DEFAULT=38
    BREAK=39
    BOOLEAN=40
    FLOAT_NUMBER=41
    DECIMAL_INTEGER=42
    STRING=43
    NAME=44
    COMMENT=45
    NEWLINE=46
    WS=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ListLangParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.NEWLINE)
            else:
                return self.getToken(ListLangParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(ListLangParser.StatementContext,i)


        def getRuleIndex(self):
            return ListLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ListLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.match(ListLangParser.NEWLINE) 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 105118930305056) != 0):
                self.state = 56
                self.statement()

                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 57
                        self.match(ListLangParser.NEWLINE) 
                    self.state = 62
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(ListLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_stmt(self):
            return self.getTypedRuleContext(ListLangParser.Expression_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(ListLangParser.Assignment_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ListLangParser.Return_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ListLangParser.Break_stmtContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmt" ):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmt(self):

        localctx = ListLangParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_simple_stmt)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.expression_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.return_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.break_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def target_list(self):
            return self.getTypedRuleContext(ListLangParser.Target_listContext,0)


        def ASSIGNMENT(self):
            return self.getToken(ListLangParser.ASSIGNMENT, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ListLangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_assignment_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_stmt" ):
                listener.enterAssignment_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_stmt" ):
                listener.exitAssignment_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = ListLangParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.target_list()
            self.state = 77
            self.match(ListLangParser.ASSIGNMENT)
            self.state = 78
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Target_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.NAME)
            else:
                return self.getToken(ListLangParser.NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.COMMA)
            else:
                return self.getToken(ListLangParser.COMMA, i)

        def getRuleIndex(self):
            return ListLangParser.RULE_target_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget_list" ):
                listener.enterTarget_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget_list" ):
                listener.exitTarget_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget_list" ):
                return visitor.visitTarget_list(self)
            else:
                return visitor.visitChildren(self)




    def target_list(self):

        localctx = ListLangParser.Target_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_target_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ListLangParser.NAME)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 81
                self.match(ListLangParser.COMMA)
                self.state = 82
                self.match(ListLangParser.NAME)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ListLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_expression_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_stmt" ):
                listener.enterExpression_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_stmt" ):
                listener.exitExpression_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_stmt" ):
                return visitor.visitExpression_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expression_stmt(self):

        localctx = ListLangParser.Expression_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ListLangParser.RETURN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ListLangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ListLangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ListLangParser.RETURN)
            self.state = 91
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ListLangParser.BREAK, 0)

        def getRuleIndex(self):
            return ListLangParser.RULE_break_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stmt" ):
                listener.enterBreak_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stmt" ):
                listener.exitBreak_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ListLangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ListLangParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(ListLangParser.Func_declContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ListLangParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(ListLangParser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ListLangParser.For_statementContext,0)


        def switch_statement(self):
            return self.getTypedRuleContext(ListLangParser.Switch_statementContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_compound_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_statement" ):
                listener.enterCompound_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_statement" ):
                listener.exitCompound_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_statement" ):
                return visitor.visitCompound_statement(self)
            else:
                return visitor.visitChildren(self)




    def compound_statement(self):

        localctx = ListLangParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_compound_statement)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.func_decl()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.if_statement()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.while_statement()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.for_statement()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.switch_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuiteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(ListLangParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.NEWLINE)
            else:
                return self.getToken(ListLangParser.NEWLINE, i)

        def INDENT(self):
            return self.getToken(ListLangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(ListLangParser.DEDENT, 0)

        def getRuleIndex(self):
            return ListLangParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuite" ):
                return visitor.visitSuite(self)
            else:
                return visitor.visitChildren(self)




    def suite(self):

        localctx = ListLangParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.statement()
                self.state = 103
                self.match(ListLangParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 105
                    self.match(ListLangParser.NEWLINE)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==46):
                        break

                self.state = 110
                self.match(ListLangParser.INDENT)
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 111
                    self.statement()
                    self.state = 114 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 105118930305056) != 0)):
                        break

                self.state = 116
                self.match(ListLangParser.DEDENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(ListLangParser.Stmt_listContext,0)


        def NEWLINE(self):
            return self.getToken(ListLangParser.NEWLINE, 0)

        def compound_statement(self):
            return self.getTypedRuleContext(ListLangParser.Compound_statementContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ListLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 23, 27, 30, 39, 40, 41, 42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.stmt_list()
                self.state = 121
                self.match(ListLangParser.NEWLINE)
                pass
            elif token in [29, 31, 33, 35, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.compound_statement()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(ListLangParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.Simple_stmtContext)
            else:
                return self.getTypedRuleContext(ListLangParser.Simple_stmtContext,i)


        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.SEMI_COLON)
            else:
                return self.getToken(ListLangParser.SEMI_COLON, i)

        def getRuleIndex(self):
            return ListLangParser.RULE_stmt_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_list" ):
                listener.enterStmt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_list" ):
                listener.exitStmt_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ListLangParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.simple_stmt()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 128
                self.match(ListLangParser.SEMI_COLON)
                self.state = 129
                self.simple_stmt()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ListLangParser.FUNC, 0)

        def NAME(self):
            return self.getToken(ListLangParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLangParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ListLangParser.CLOSE_PAREN, 0)

        def COLON(self):
            return self.getToken(ListLangParser.COLON, 0)

        def suite(self):
            return self.getTypedRuleContext(ListLangParser.SuiteContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(ListLangParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ListLangParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ListLangParser.FUNC)
            self.state = 136
            self.match(ListLangParser.NAME)
            self.state = 137
            self.match(ListLangParser.OPEN_PAREN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==44:
                self.state = 138
                self.parameter_list()


            self.state = 141
            self.match(ListLangParser.CLOSE_PAREN)
            self.state = 142
            self.match(ListLangParser.COLON)
            self.state = 143
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(ListLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.COMMA)
            else:
                return self.getToken(ListLangParser.COMMA, i)

        def getRuleIndex(self):
            return ListLangParser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ListLangParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.param()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 146
                self.match(ListLangParser.COMMA)
                self.state = 147
                self.param()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(ListLangParser.NAME, 0)

        def AMP(self):
            return self.getToken(ListLangParser.AMP, 0)

        def getRuleIndex(self):
            return ListLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ListLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 153
                self.match(ListLangParser.AMP)


            self.state = 156
            self.match(ListLangParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ListLangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(ListLangParser.ExpressionContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.COLON)
            else:
                return self.getToken(ListLangParser.COLON, i)

        def suite(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.SuiteContext)
            else:
                return self.getTypedRuleContext(ListLangParser.SuiteContext,i)


        def ELSE(self):
            return self.getToken(ListLangParser.ELSE, 0)

        def getRuleIndex(self):
            return ListLangParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ListLangParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ListLangParser.IF)
            self.state = 159
            self.expression(0)
            self.state = 160
            self.match(ListLangParser.COLON)
            self.state = 161
            self.suite()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 162
                self.match(ListLangParser.ELSE)
                self.state = 163
                self.match(ListLangParser.COLON)
                self.state = 164
                self.suite()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ListLangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(ListLangParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(ListLangParser.COLON, 0)

        def suite(self):
            return self.getTypedRuleContext(ListLangParser.SuiteContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = ListLangParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(ListLangParser.WHILE)
            self.state = 168
            self.expression(0)
            self.state = 169
            self.match(ListLangParser.COLON)
            self.state = 170
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ListLangParser.FOR, 0)

        def target_list(self):
            return self.getTypedRuleContext(ListLangParser.Target_listContext,0)


        def IN(self):
            return self.getToken(ListLangParser.IN, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ListLangParser.Expression_listContext,0)


        def COLON(self):
            return self.getToken(ListLangParser.COLON, 0)

        def suite(self):
            return self.getTypedRuleContext(ListLangParser.SuiteContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ListLangParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ListLangParser.FOR)
            self.state = 173
            self.target_list()
            self.state = 174
            self.match(ListLangParser.IN)
            self.state = 175
            self.expression_list()
            self.state = 176
            self.match(ListLangParser.COLON)
            self.state = 177
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(ListLangParser.SWITCH, 0)

        def expression(self):
            return self.getTypedRuleContext(ListLangParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(ListLangParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(ListLangParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(ListLangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(ListLangParser.DEDENT, 0)

        def case_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.Case_blockContext)
            else:
                return self.getTypedRuleContext(ListLangParser.Case_blockContext,i)


        def default_block(self):
            return self.getTypedRuleContext(ListLangParser.Default_blockContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_switch_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_statement" ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_statement" ):
                listener.exitSwitch_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_statement" ):
                return visitor.visitSwitch_statement(self)
            else:
                return visitor.visitChildren(self)




    def switch_statement(self):

        localctx = ListLangParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_switch_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ListLangParser.SWITCH)
            self.state = 180
            self.expression(0)
            self.state = 181
            self.match(ListLangParser.COLON)
            self.state = 182
            self.match(ListLangParser.NEWLINE)
            self.state = 183
            self.match(ListLangParser.INDENT)
            self.state = 185 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 184
                self.case_block()
                self.state = 187 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 189
                self.default_block()


            self.state = 192
            self.match(ListLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(ListLangParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(ListLangParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(ListLangParser.COLON, 0)

        def suite(self):
            return self.getTypedRuleContext(ListLangParser.SuiteContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_case_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_block" ):
                listener.enterCase_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_block" ):
                listener.exitCase_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_block" ):
                return visitor.visitCase_block(self)
            else:
                return visitor.visitChildren(self)




    def case_block(self):

        localctx = ListLangParser.Case_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_case_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ListLangParser.CASE)
            self.state = 195
            self.expression(0)
            self.state = 196
            self.match(ListLangParser.COLON)
            self.state = 197
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(ListLangParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(ListLangParser.COLON, 0)

        def suite(self):
            return self.getTypedRuleContext(ListLangParser.SuiteContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_default_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_block" ):
                listener.enterDefault_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_block" ):
                listener.exitDefault_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_block" ):
                return visitor.visitDefault_block(self)
            else:
                return visitor.visitChildren(self)




    def default_block(self):

        localctx = ListLangParser.Default_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_default_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ListLangParser.DEFAULT)
            self.state = 200
            self.match(ListLangParser.COLON)
            self.state = 201
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ListLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.COMMA)
            else:
                return self.getToken(ListLangParser.COMMA, i)

        def getRuleIndex(self):
            return ListLangParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = ListLangParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expression(0)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 204
                self.match(ListLangParser.COMMA)
                self.state = 205
                self.expression(0)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def NOT(self):
            return self.getToken(ListLangParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ListLangParser.ExpressionContext,i)


        def atom(self):
            return self.getTypedRuleContext(ListLangParser.AtomContext,0)


        def MULT(self):
            return self.getToken(ListLangParser.MULT, 0)

        def DIV(self):
            return self.getToken(ListLangParser.DIV, 0)

        def MOD(self):
            return self.getToken(ListLangParser.MOD, 0)

        def ADD(self):
            return self.getToken(ListLangParser.ADD, 0)

        def MINUS(self):
            return self.getToken(ListLangParser.MINUS, 0)

        def EQUALS(self):
            return self.getToken(ListLangParser.EQUALS, 0)

        def NOT_EQ(self):
            return self.getToken(ListLangParser.NOT_EQ, 0)

        def LESS_THAN(self):
            return self.getToken(ListLangParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(ListLangParser.GREATER_THAN, 0)

        def LT_EQ(self):
            return self.getToken(ListLangParser.LT_EQ, 0)

        def GT_EQ(self):
            return self.getToken(ListLangParser.GT_EQ, 0)

        def AND(self):
            return self.getToken(ListLangParser.AND, 0)

        def OR(self):
            return self.getToken(ListLangParser.OR, 0)

        def getRuleIndex(self):
            return ListLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ListLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 212
                self.match(ListLangParser.NOT)
                self.state = 213
                self.expression(2)
                pass
            elif token in [23, 27, 40, 41, 42, 43, 44]:
                self.state = 214
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 229
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = ListLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 217
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 218
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = ListLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 220
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 221
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = ListLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 223
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 224
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = ListLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 226
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 227
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.expression(4)
                        pass

             
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ListLangParser.LiteralContext,0)


        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.NAME)
            else:
                return self.getToken(ListLangParser.NAME, i)

        def DOT(self):
            return self.getToken(ListLangParser.DOT, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLangParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ListLangParser.CLOSE_PAREN, 0)

        def arg_list(self):
            return self.getTypedRuleContext(ListLangParser.Arg_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(ListLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ListLangParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ListLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(ListLangParser.NAME)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(ListLangParser.NAME)
                self.state = 237
                self.match(ListLangParser.DOT)
                self.state = 238
                self.match(ListLangParser.NAME)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.match(ListLangParser.NAME)
                self.state = 240
                self.match(ListLangParser.DOT)
                self.state = 241
                self.match(ListLangParser.NAME)
                self.state = 242
                self.match(ListLangParser.OPEN_PAREN)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34085003067424) != 0):
                    self.state = 243
                    self.arg_list()


                self.state = 246
                self.match(ListLangParser.CLOSE_PAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.match(ListLangParser.NAME)
                self.state = 248
                self.match(ListLangParser.OPEN_PAREN)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34085003067424) != 0):
                    self.state = 249
                    self.arg_list()


                self.state = 252
                self.match(ListLangParser.CLOSE_PAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.match(ListLangParser.OPEN_PAREN)
                self.state = 254
                self.expression(0)
                self.state = 255
                self.match(ListLangParser.CLOSE_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ListLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLangParser.COMMA)
            else:
                return self.getToken(ListLangParser.COMMA, i)

        def getRuleIndex(self):
            return ListLangParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = ListLangParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.expression(0)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 260
                self.match(ListLangParser.COMMA)
                self.state = 261
                self.expression(0)
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_INTEGER(self):
            return self.getToken(ListLangParser.DECIMAL_INTEGER, 0)

        def FLOAT_NUMBER(self):
            return self.getToken(ListLangParser.FLOAT_NUMBER, 0)

        def STRING(self):
            return self.getToken(ListLangParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(ListLangParser.BOOLEAN, 0)

        def OPEN_BRACKET(self):
            return self.getToken(ListLangParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(ListLangParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ListLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ListLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(ListLangParser.DECIMAL_INTEGER)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(ListLangParser.FLOAT_NUMBER)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(ListLangParser.STRING)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 270
                self.match(ListLangParser.BOOLEAN)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 271
                self.match(ListLangParser.OPEN_BRACKET)
                self.state = 272
                self.match(ListLangParser.CLOSE_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




