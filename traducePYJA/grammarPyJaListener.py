# Generated from grammarPyJa.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarPyJaParser import grammarPyJaParser
else:
    from grammarPyJaParser import grammarPyJaParser

# This class defines a complete listener for a parse tree produced by grammarPyJaParser.
class grammarPyJaListener(ParseTreeListener):

    # Enter a parse tree produced by grammarPyJaParser#program.
    def enterProgram(self, ctx:grammarPyJaParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#program.
    def exitProgram(self, ctx:grammarPyJaParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:grammarPyJaParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:grammarPyJaParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#parameters.
    def enterParameters(self, ctx:grammarPyJaParser.ParametersContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#parameters.
    def exitParameters(self, ctx:grammarPyJaParser.ParametersContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#statement.
    def enterStatement(self, ctx:grammarPyJaParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#statement.
    def exitStatement(self, ctx:grammarPyJaParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#assignment.
    def enterAssignment(self, ctx:grammarPyJaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#assignment.
    def exitAssignment(self, ctx:grammarPyJaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#expression.
    def enterExpression(self, ctx:grammarPyJaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#expression.
    def exitExpression(self, ctx:grammarPyJaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#functionCall.
    def enterFunctionCall(self, ctx:grammarPyJaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#functionCall.
    def exitFunctionCall(self, ctx:grammarPyJaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#arguments.
    def enterArguments(self, ctx:grammarPyJaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#arguments.
    def exitArguments(self, ctx:grammarPyJaParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by grammarPyJaParser#printStatement.
    def enterPrintStatement(self, ctx:grammarPyJaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by grammarPyJaParser#printStatement.
    def exitPrintStatement(self, ctx:grammarPyJaParser.PrintStatementContext):
        pass



del grammarPyJaParser