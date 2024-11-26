# Generated from grammarPyJa.g4 by ANTLR 4.13.2
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
        4,1,13,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,4,1,34,8,1,11,1,12,1,35,1,1,1,1,1,1,1,2,1,
        2,1,2,5,2,44,8,2,10,2,12,2,47,9,2,1,3,1,3,3,3,51,8,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,3,5,60,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,68,8,5,10,
        5,12,5,71,9,5,1,6,1,6,1,6,3,6,76,8,6,1,6,1,6,1,7,1,7,1,7,5,7,83,
        8,7,10,7,12,7,86,9,7,1,8,1,8,1,8,1,8,1,8,1,8,0,1,10,9,0,2,4,6,8,
        10,12,14,16,0,0,94,0,23,1,0,0,0,2,26,1,0,0,0,4,40,1,0,0,0,6,50,1,
        0,0,0,8,52,1,0,0,0,10,59,1,0,0,0,12,72,1,0,0,0,14,79,1,0,0,0,16,
        87,1,0,0,0,18,22,3,2,1,0,19,22,3,16,8,0,20,22,3,8,4,0,21,18,1,0,
        0,0,21,19,1,0,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,1,1,0,0,0,25,23,1,0,0,0,26,27,5,1,0,0,27,28,5,4,0,0,28,
        29,5,7,0,0,29,30,3,4,2,0,30,31,5,8,0,0,31,33,5,10,0,0,32,34,3,6,
        3,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,
        1,0,0,0,37,38,5,2,0,0,38,39,3,10,5,0,39,3,1,0,0,0,40,45,5,4,0,0,
        41,42,5,9,0,0,42,44,5,4,0,0,43,41,1,0,0,0,44,47,1,0,0,0,45,43,1,
        0,0,0,45,46,1,0,0,0,46,5,1,0,0,0,47,45,1,0,0,0,48,51,3,8,4,0,49,
        51,3,16,8,0,50,48,1,0,0,0,50,49,1,0,0,0,51,7,1,0,0,0,52,53,5,4,0,
        0,53,54,5,13,0,0,54,55,3,10,5,0,55,9,1,0,0,0,56,57,6,5,-1,0,57,60,
        5,4,0,0,58,60,5,5,0,0,59,56,1,0,0,0,59,58,1,0,0,0,60,69,1,0,0,0,
        61,62,10,4,0,0,62,63,5,11,0,0,63,68,3,10,5,5,64,65,10,3,0,0,65,66,
        5,12,0,0,66,68,3,10,5,4,67,61,1,0,0,0,67,64,1,0,0,0,68,71,1,0,0,
        0,69,67,1,0,0,0,69,70,1,0,0,0,70,11,1,0,0,0,71,69,1,0,0,0,72,73,
        5,4,0,0,73,75,5,7,0,0,74,76,3,14,7,0,75,74,1,0,0,0,75,76,1,0,0,0,
        76,77,1,0,0,0,77,78,5,8,0,0,78,13,1,0,0,0,79,84,3,10,5,0,80,81,5,
        9,0,0,81,83,3,10,5,0,82,80,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,
        85,1,0,0,0,85,15,1,0,0,0,86,84,1,0,0,0,87,88,5,3,0,0,88,89,5,7,0,
        0,89,90,3,10,5,0,90,91,5,8,0,0,91,17,1,0,0,0,10,21,23,35,45,50,59,
        67,69,75,84
    ]

class grammarPyJaParser ( Parser ):

    grammarFileName = "grammarPyJa.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "','", "':'", 
                     "'*'", "'-'", "'='" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "IDENTIFIER", 
                      "NUMBER", "WS", "LPAREN", "RPAREN", "COMMA", "COLON", 
                      "ASTERISK", "MINUS", "ASSIGN" ]

    RULE_program = 0
    RULE_functionDefinition = 1
    RULE_parameters = 2
    RULE_statement = 3
    RULE_assignment = 4
    RULE_expression = 5
    RULE_functionCall = 6
    RULE_arguments = 7
    RULE_printStatement = 8

    ruleNames =  [ "program", "functionDefinition", "parameters", "statement", 
                   "assignment", "expression", "functionCall", "arguments", 
                   "printStatement" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    IDENTIFIER=4
    NUMBER=5
    WS=6
    LPAREN=7
    RPAREN=8
    COMMA=9
    COLON=10
    ASTERISK=11
    MINUS=12
    ASSIGN=13

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

        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarPyJaParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(grammarPyJaParser.FunctionDefinitionContext,i)


        def printStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarPyJaParser.PrintStatementContext)
            else:
                return self.getTypedRuleContext(grammarPyJaParser.PrintStatementContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarPyJaParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(grammarPyJaParser.AssignmentContext,i)


        def getRuleIndex(self):
            return grammarPyJaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = grammarPyJaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26) != 0):
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 18
                    self.functionDefinition()
                    pass
                elif token in [3]:
                    self.state = 19
                    self.printStatement()
                    pass
                elif token in [4]:
                    self.state = 20
                    self.assignment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(grammarPyJaParser.DEF, 0)

        def IDENTIFIER(self):
            return self.getToken(grammarPyJaParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(grammarPyJaParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(grammarPyJaParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(grammarPyJaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(grammarPyJaParser.COLON, 0)

        def RETURN(self):
            return self.getToken(grammarPyJaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarPyJaParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarPyJaParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarPyJaParser.StatementContext,i)


        def getRuleIndex(self):
            return grammarPyJaParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = grammarPyJaParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(grammarPyJaParser.DEF)
            self.state = 27
            self.match(grammarPyJaParser.IDENTIFIER)
            self.state = 28
            self.match(grammarPyJaParser.LPAREN)
            self.state = 29
            self.parameters()
            self.state = 30
            self.match(grammarPyJaParser.RPAREN)
            self.state = 31
            self.match(grammarPyJaParser.COLON)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==4):
                    break

            self.state = 37
            self.match(grammarPyJaParser.RETURN)
            self.state = 38
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(grammarPyJaParser.IDENTIFIER)
            else:
                return self.getToken(grammarPyJaParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarPyJaParser.COMMA)
            else:
                return self.getToken(grammarPyJaParser.COMMA, i)

        def getRuleIndex(self):
            return grammarPyJaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = grammarPyJaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(grammarPyJaParser.IDENTIFIER)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 41
                self.match(grammarPyJaParser.COMMA)
                self.state = 42
                self.match(grammarPyJaParser.IDENTIFIER)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def assignment(self):
            return self.getTypedRuleContext(grammarPyJaParser.AssignmentContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(grammarPyJaParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return grammarPyJaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = grammarPyJaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.printStatement()
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(grammarPyJaParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(grammarPyJaParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarPyJaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammarPyJaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = grammarPyJaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(grammarPyJaParser.IDENTIFIER)
            self.state = 53
            self.match(grammarPyJaParser.ASSIGN)
            self.state = 54
            self.expression(0)
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

        def IDENTIFIER(self):
            return self.getToken(grammarPyJaParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(grammarPyJaParser.NUMBER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarPyJaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grammarPyJaParser.ExpressionContext,i)


        def ASTERISK(self):
            return self.getToken(grammarPyJaParser.ASTERISK, 0)

        def MINUS(self):
            return self.getToken(grammarPyJaParser.MINUS, 0)

        def getRuleIndex(self):
            return grammarPyJaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarPyJaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 57
                self.match(grammarPyJaParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.state = 58
                self.match(grammarPyJaParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 67
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = grammarPyJaParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 61
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 62
                        self.match(grammarPyJaParser.ASTERISK)
                        self.state = 63
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = grammarPyJaParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 65
                        self.match(grammarPyJaParser.MINUS)
                        self.state = 66
                        self.expression(4)
                        pass

             
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(grammarPyJaParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(grammarPyJaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(grammarPyJaParser.RPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(grammarPyJaParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return grammarPyJaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = grammarPyJaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(grammarPyJaParser.IDENTIFIER)
            self.state = 73
            self.match(grammarPyJaParser.LPAREN)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==5:
                self.state = 74
                self.arguments()


            self.state = 77
            self.match(grammarPyJaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarPyJaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grammarPyJaParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarPyJaParser.COMMA)
            else:
                return self.getToken(grammarPyJaParser.COMMA, i)

        def getRuleIndex(self):
            return grammarPyJaParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = grammarPyJaParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.expression(0)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 80
                self.match(grammarPyJaParser.COMMA)
                self.state = 81
                self.expression(0)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(grammarPyJaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(grammarPyJaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarPyJaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarPyJaParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarPyJaParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = grammarPyJaParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(grammarPyJaParser.PRINT)
            self.state = 88
            self.match(grammarPyJaParser.LPAREN)
            self.state = 89
            self.expression(0)
            self.state = 90
            self.match(grammarPyJaParser.RPAREN)
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
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




