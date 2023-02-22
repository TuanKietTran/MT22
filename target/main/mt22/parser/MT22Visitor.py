# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#compilationUnit.
    def visitCompilationUnit(self, ctx:MT22Parser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#translationUnit.
    def visitTranslationUnit(self, ctx:MT22Parser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:MT22Parser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifierList.
    def visitIdentifierList(self, ctx:MT22Parser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortDeclaration.
    def visitShortDeclaration(self, ctx:MT22Parser.ShortDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fullDeclaration.
    def visitFullDeclaration(self, ctx:MT22Parser.FullDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MT22Parser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramDeclarator.
    def visitParamDeclarator(self, ctx:MT22Parser.ParamDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritance.
    def visitInheritance(self, ctx:MT22Parser.InheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterList.
    def visitParameterList(self, ctx:MT22Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:MT22Parser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#voidType.
    def visitVoidType(self, ctx:MT22Parser.VoidTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#compoundStatement.
    def visitCompoundStatement(self, ctx:MT22Parser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockItemList.
    def visitBlockItemList(self, ctx:MT22Parser.BlockItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockItem.
    def visitBlockItem(self, ctx:MT22Parser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionStatement.
    def visitExpressionStatement(self, ctx:MT22Parser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#selectionStatement.
    def visitSelectionStatement(self, ctx:MT22Parser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#iterationStatement.
    def visitIterationStatement(self, ctx:MT22Parser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forCondition.
    def visitForCondition(self, ctx:MT22Parser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forDeclaration.
    def visitForDeclaration(self, ctx:MT22Parser.ForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#conditionExpression.
    def visitConditionExpression(self, ctx:MT22Parser.ConditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#updateExpression.
    def visitUpdateExpression(self, ctx:MT22Parser.UpdateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#jumpStatement.
    def visitJumpStatement(self, ctx:MT22Parser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MT22Parser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringExpression.
    def visitStringExpression(self, ctx:MT22Parser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:MT22Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalExpression.
    def visitLogicalExpression(self, ctx:MT22Parser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MT22Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MT22Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:MT22Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unaryOperator.
    def visitUnaryOperator(self, ctx:MT22Parser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MT22Parser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#postfixExpression.
    def visitPostfixExpression(self, ctx:MT22Parser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)



del MT22Parser