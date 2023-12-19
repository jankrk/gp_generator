// Generated from c:/Users/ISI/Documents/Semestr5/Programowanie genetyczne (blok 1S)/GP_Generator/gp_generator/antlr/GPMini.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GPMiniParser}.
 */
public interface GPMiniListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(GPMiniParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(GPMiniParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(GPMiniParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(GPMiniParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void enterStatementBlock(GPMiniParser.StatementBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void exitStatementBlock(GPMiniParser.StatementBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoopStatement(GPMiniParser.LoopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoopStatement(GPMiniParser.LoopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#conditionalStatement}.
	 * @param ctx the parse tree
	 */
	void enterConditionalStatement(GPMiniParser.ConditionalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#conditionalStatement}.
	 * @param ctx the parse tree
	 */
	void exitConditionalStatement(GPMiniParser.ConditionalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(GPMiniParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(GPMiniParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(GPMiniParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(GPMiniParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#inputStatement}.
	 * @param ctx the parse tree
	 */
	void enterInputStatement(GPMiniParser.InputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#inputStatement}.
	 * @param ctx the parse tree
	 */
	void exitInputStatement(GPMiniParser.InputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#outputStatement}.
	 * @param ctx the parse tree
	 */
	void enterOutputStatement(GPMiniParser.OutputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#outputStatement}.
	 * @param ctx the parse tree
	 */
	void exitOutputStatement(GPMiniParser.OutputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(GPMiniParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(GPMiniParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#variableStatement}.
	 * @param ctx the parse tree
	 */
	void enterVariableStatement(GPMiniParser.VariableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#variableStatement}.
	 * @param ctx the parse tree
	 */
	void exitVariableStatement(GPMiniParser.VariableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(GPMiniParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(GPMiniParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#numericExpression}.
	 * @param ctx the parse tree
	 */
	void enterNumericExpression(GPMiniParser.NumericExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#numericExpression}.
	 * @param ctx the parse tree
	 */
	void exitNumericExpression(GPMiniParser.NumericExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#numericTerm}.
	 * @param ctx the parse tree
	 */
	void enterNumericTerm(GPMiniParser.NumericTermContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#numericTerm}.
	 * @param ctx the parse tree
	 */
	void exitNumericTerm(GPMiniParser.NumericTermContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#numericFactor}.
	 * @param ctx the parse tree
	 */
	void enterNumericFactor(GPMiniParser.NumericFactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#numericFactor}.
	 * @param ctx the parse tree
	 */
	void exitNumericFactor(GPMiniParser.NumericFactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#numericAtomValue}.
	 * @param ctx the parse tree
	 */
	void enterNumericAtomValue(GPMiniParser.NumericAtomValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#numericAtomValue}.
	 * @param ctx the parse tree
	 */
	void exitNumericAtomValue(GPMiniParser.NumericAtomValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#logicExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicExpression(GPMiniParser.LogicExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#logicExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicExpression(GPMiniParser.LogicExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#logicTerm}.
	 * @param ctx the parse tree
	 */
	void enterLogicTerm(GPMiniParser.LogicTermContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#logicTerm}.
	 * @param ctx the parse tree
	 */
	void exitLogicTerm(GPMiniParser.LogicTermContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#logicComparison}.
	 * @param ctx the parse tree
	 */
	void enterLogicComparison(GPMiniParser.LogicComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#logicComparison}.
	 * @param ctx the parse tree
	 */
	void exitLogicComparison(GPMiniParser.LogicComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#logicFactor}.
	 * @param ctx the parse tree
	 */
	void enterLogicFactor(GPMiniParser.LogicFactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#logicFactor}.
	 * @param ctx the parse tree
	 */
	void exitLogicFactor(GPMiniParser.LogicFactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#logicAtomValue}.
	 * @param ctx the parse tree
	 */
	void enterLogicAtomValue(GPMiniParser.LogicAtomValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#logicAtomValue}.
	 * @param ctx the parse tree
	 */
	void exitLogicAtomValue(GPMiniParser.LogicAtomValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#numericComparison}.
	 * @param ctx the parse tree
	 */
	void enterNumericComparison(GPMiniParser.NumericComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#numericComparison}.
	 * @param ctx the parse tree
	 */
	void exitNumericComparison(GPMiniParser.NumericComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOperator(GPMiniParser.ComparisonOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#comparisonOperator}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOperator(GPMiniParser.ComparisonOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#numericValue}.
	 * @param ctx the parse tree
	 */
	void enterNumericValue(GPMiniParser.NumericValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#numericValue}.
	 * @param ctx the parse tree
	 */
	void exitNumericValue(GPMiniParser.NumericValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link GPMiniParser#logicValue}.
	 * @param ctx the parse tree
	 */
	void enterLogicValue(GPMiniParser.LogicValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GPMiniParser#logicValue}.
	 * @param ctx the parse tree
	 */
	void exitLogicValue(GPMiniParser.LogicValueContext ctx);
}