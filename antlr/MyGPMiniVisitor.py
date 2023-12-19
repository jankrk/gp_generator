# Generated from GPMini.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GPMiniParser import GPMiniParser
    from .GPMiniVisitor import GPMiniVisitor
else:
    from GPMiniParser import GPMiniParser
    from GPMiniVisitor import GPMiniVisitor

# This class defines a complete generic visitor for a parse tree produced by GPMiniParser.

class MyGPMiniVisitor(GPMiniVisitor):
    def __init__(self, counter, input):
        self.variableList = []
        self.breakValue = []
        self.counter = counter
        self.input = input
        self.inputIndex = 0
        self.output = []

    # Visit a parse tree produced by GPMiniParser#program.
    def visitProgram(self, ctx:GPMiniParser.ProgramContext):
        for s in ctx.statement():
            if self.counter == 0:
                return self.output
            self.visitStatement(s)
        return self.output


    # Visit a parse tree produced by GPMiniParser#statement.
    def visitStatement(self, ctx:GPMiniParser.StatementContext):
        self.counter -= 1
        next_child_rule_name = ctx.parser.ruleNames[ctx.getChild(0).getRuleIndex()]
        
        match next_child_rule_name:
            case 'loopStatement' : 
                self.visitLoopStatement(ctx.loopStatement())
            
            case 'conditionalStatement' :
                self.visitConditionalStatement(ctx.conditionalStatement())

            case 'outputStatement' :
                self.visitOutputStatement(ctx.outputStatement())
            
            case 'variableStatement':
                self.visitVariableStatement(ctx.variableStatement())

            case _:
                return 'error'
        return


    # Visit a parse tree produced by GPMiniParser#statementBlock.
    def visitStatementBlock(self, ctx:GPMiniParser.StatementBlockContext):
        next_child_rule_name = ctx.parser.ruleNames[ctx.getChild(0).getRuleIndex()]
        self.counter -= 1
        
        match next_child_rule_name:
            case 'loopStatement' : 
                self.visitLoopStatement(ctx.loopStatement())
            
            case 'conditionalStatement' :
                self.visitConditionalStatement(ctx.conditionalStatement())

            case 'outputStatement' :
                self.visitOutputStatement(ctx.outputStatement())
            
            case 'variableStatement':
                self.visitVariableStatement(ctx.variableStatement())

            case 'breakStatement':
                self.visitBreakStatement(ctx.breakStatement())

            case _:
                return 'error'
        return


    # Visit a parse tree produced by GPMiniParser#loopStatement.
    def visitLoopStatement(self, ctx:GPMiniParser.LoopStatementContext):
        self.breakValue.append(False)
        while self.value_eval(ctx.expression().getText(), self.visitExpression(ctx.expression())) and not self.breakValue[-1]:
            if self.counter == 0:
                return
            self.visitBlock(ctx.block())
        self.breakValue.pop()
        return


    # Visit a parse tree produced by GPMiniParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:GPMiniParser.ConditionalStatementContext):
        if self.value_eval(ctx.expression().getText(), self.visitExpression(ctx.expression())):
            self.visitBlock(ctx.getChild(4))
        return


    # Visit a parse tree produced by GPMiniParser#block.
    def visitBlock(self, ctx:GPMiniParser.BlockContext):
        self.counter -= 1
        for s in ctx.statementBlock():
            if self.counter == 0:
                return
            self.visitStatementBlock(s)

        return


    # Visit a parse tree produced by GPMiniParser#breakStatement.
    def visitBreakStatement(self, ctx:GPMiniParser.BreakStatementContext):
        self.breakValue[-1] = True
        return


    # Visit a parse tree produced by GPMiniParser#inputStatement.
    def visitInputStatement(self, ctx:GPMiniParser.InputStatementContext):
        if self.inputIndex < len(self.input):
            self.inputIndex += 1
            return self.input[self.inputIndex-1]
        return 0


    # Visit a parse tree produced by GPMiniParser#outputStatement.
    def visitOutputStatement(self, ctx:GPMiniParser.OutputStatementContext):
        output = self.value_eval(ctx.expression().getText(), self.visitExpression(ctx.expression()))
        self.output.append(int(output))
        return


    # Visit a parse tree produced by GPMiniParser#variable.
    def visitVariable(self, ctx:GPMiniParser.VariableContext):
        variable_name = ctx.getText()
        index = int(variable_name[3::])
        if index < len(self.variableList):
            return self.variableList[index]
        else:
            return 0


    # Visit a parse tree produced by GPMiniParser#variableStatement.
    def visitVariableStatement(self, ctx:GPMiniParser.VariableStatementContext):
        index = int(ctx.variable().getText()[3::])
        value = self.value_eval(ctx.expression().getText(), self.visitExpression(ctx.expression()))

        if len(self.variableList) < index+1:
            b = []
            for i in range(index+1):
                if len(self.variableList)>i:
                    b.append(self.variableList[i])
                else:
                    b.append(0)
            b[index] = value
            self.variableList = b
        else:
            self.variableList[index]=value
        return


    # Visit a parse tree produced by GPMiniParser#expression.
    def visitExpression(self, ctx:GPMiniParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return f'({self.visitExpression(ctx.getChild(1))})'
            else:
                left = self.visitExpression(ctx.getChild(0))
                right = self.visitExpression(ctx.getChild(2))
                operator = ctx.getChild(1).getText()
                return f'{left} {operator} {right}'
        elif ctx.getChildCount() == 2:
            operator = ctx.getChild(0).getText()
            if operator == 'not':
                return f'{operator} {self.visitExpression(ctx.getChild(1))}'
            else:
                return f'{operator} {self.visitValue(ctx.getChild(1))}'
        else:
            return f'{self.visitValue(ctx.getChild(0))}'


    # Visit a parse tree produced by GPMiniParser#value.
    def visitValue(self, ctx:GPMiniParser.ValueContext):
        next_child_rule_name = ctx.parser.ruleNames[ctx.getChild(0).getRuleIndex()]

        match next_child_rule_name:
            case 'variable' :
                return self.visitVariable(ctx.variable())
            case 'numericValue' :
                return self.visitNumericValue(ctx.numericValue())
            case 'logicValue' :
                return self.visitLogicValue(ctx.logicValue())
            case 'inputStatement' :
                return self.visitInputStatement(ctx.inputStatement())
            case _: 
                return
            

    # Visit a parse tree produced by GPMiniParser#numericValue.
    def visitNumericValue(self, ctx:GPMiniParser.NumericValueContext):
        return ctx.getText()


    # Visit a parse tree produced by GPMiniParser#logicValue.
    def visitLogicValue(self, ctx:GPMiniParser.LogicValueContext):
        return True if ctx.getText() == 'true' else False
    
    def value_eval(self, orginal, string):
        try:
            return eval(string)
        except Exception as error:
            self.output = ['ERROR', error, orginal, string]
            self.counter = 0
            return 0

del GPMiniParser