# Generated from GPMini.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GPMiniParser import GPMiniParser
else:
    from GPMiniParser import GPMiniParser

# This class defines a complete generic visitor for a parse tree produced by GPMiniParser.

class GPMiniVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GPMiniParser#program.
    def visitProgram(self, ctx:GPMiniParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#statement.
    def visitStatement(self, ctx:GPMiniParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#statementBlock.
    def visitStatementBlock(self, ctx:GPMiniParser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#loopStatement.
    def visitLoopStatement(self, ctx:GPMiniParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:GPMiniParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#block.
    def visitBlock(self, ctx:GPMiniParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#breakStatement.
    def visitBreakStatement(self, ctx:GPMiniParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#inputStatement.
    def visitInputStatement(self, ctx:GPMiniParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#outputStatement.
    def visitOutputStatement(self, ctx:GPMiniParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#variable.
    def visitVariable(self, ctx:GPMiniParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#variableStatement.
    def visitVariableStatement(self, ctx:GPMiniParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#expression.
    def visitExpression(self, ctx:GPMiniParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#value.
    def visitValue(self, ctx:GPMiniParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#numericValue.
    def visitNumericValue(self, ctx:GPMiniParser.NumericValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GPMiniParser#logicValue.
    def visitLogicValue(self, ctx:GPMiniParser.LogicValueContext):
        return self.visitChildren(ctx)



del GPMiniParser