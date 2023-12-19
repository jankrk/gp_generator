# Generated from GPMini.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GPMiniParser import GPMiniParser
else:
    from GPMiniParser import GPMiniParser

# This class defines a complete listener for a parse tree produced by GPMiniParser.
class GPMiniListener(ParseTreeListener):

    # Enter a parse tree produced by GPMiniParser#program.
    def enterProgram(self, ctx:GPMiniParser.ProgramContext):
        pass

    # Exit a parse tree produced by GPMiniParser#program.
    def exitProgram(self, ctx:GPMiniParser.ProgramContext):
        pass


    # Enter a parse tree produced by GPMiniParser#statement.
    def enterStatement(self, ctx:GPMiniParser.StatementContext):
        pass

    # Exit a parse tree produced by GPMiniParser#statement.
    def exitStatement(self, ctx:GPMiniParser.StatementContext):
        pass


    # Enter a parse tree produced by GPMiniParser#statementBlock.
    def enterStatementBlock(self, ctx:GPMiniParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by GPMiniParser#statementBlock.
    def exitStatementBlock(self, ctx:GPMiniParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by GPMiniParser#loopStatement.
    def enterLoopStatement(self, ctx:GPMiniParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by GPMiniParser#loopStatement.
    def exitLoopStatement(self, ctx:GPMiniParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by GPMiniParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:GPMiniParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by GPMiniParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:GPMiniParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by GPMiniParser#block.
    def enterBlock(self, ctx:GPMiniParser.BlockContext):
        pass

    # Exit a parse tree produced by GPMiniParser#block.
    def exitBlock(self, ctx:GPMiniParser.BlockContext):
        pass


    # Enter a parse tree produced by GPMiniParser#breakStatement.
    def enterBreakStatement(self, ctx:GPMiniParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by GPMiniParser#breakStatement.
    def exitBreakStatement(self, ctx:GPMiniParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by GPMiniParser#inputStatement.
    def enterInputStatement(self, ctx:GPMiniParser.InputStatementContext):
        pass

    # Exit a parse tree produced by GPMiniParser#inputStatement.
    def exitInputStatement(self, ctx:GPMiniParser.InputStatementContext):
        pass


    # Enter a parse tree produced by GPMiniParser#outputStatement.
    def enterOutputStatement(self, ctx:GPMiniParser.OutputStatementContext):
        pass

    # Exit a parse tree produced by GPMiniParser#outputStatement.
    def exitOutputStatement(self, ctx:GPMiniParser.OutputStatementContext):
        pass


    # Enter a parse tree produced by GPMiniParser#variable.
    def enterVariable(self, ctx:GPMiniParser.VariableContext):
        pass

    # Exit a parse tree produced by GPMiniParser#variable.
    def exitVariable(self, ctx:GPMiniParser.VariableContext):
        pass


    # Enter a parse tree produced by GPMiniParser#variableStatement.
    def enterVariableStatement(self, ctx:GPMiniParser.VariableStatementContext):
        pass

    # Exit a parse tree produced by GPMiniParser#variableStatement.
    def exitVariableStatement(self, ctx:GPMiniParser.VariableStatementContext):
        pass


    # Enter a parse tree produced by GPMiniParser#expression.
    def enterExpression(self, ctx:GPMiniParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GPMiniParser#expression.
    def exitExpression(self, ctx:GPMiniParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GPMiniParser#value.
    def enterValue(self, ctx:GPMiniParser.ValueContext):
        pass

    # Exit a parse tree produced by GPMiniParser#value.
    def exitValue(self, ctx:GPMiniParser.ValueContext):
        pass


    # Enter a parse tree produced by GPMiniParser#numericValue.
    def enterNumericValue(self, ctx:GPMiniParser.NumericValueContext):
        pass

    # Exit a parse tree produced by GPMiniParser#numericValue.
    def exitNumericValue(self, ctx:GPMiniParser.NumericValueContext):
        pass


    # Enter a parse tree produced by GPMiniParser#logicValue.
    def enterLogicValue(self, ctx:GPMiniParser.LogicValueContext):
        pass

    # Exit a parse tree produced by GPMiniParser#logicValue.
    def exitLogicValue(self, ctx:GPMiniParser.LogicValueContext):
        pass



del GPMiniParser