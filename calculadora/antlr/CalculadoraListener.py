# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from calculadora.antlr.CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#program.
    def enterProgram(self, ctx:CalculadoraParser.ProgramContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#program.
    def exitProgram(self, ctx:CalculadoraParser.ProgramContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#assignStatement.
    def enterAssignStatement(self, ctx:CalculadoraParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#assignStatement.
    def exitAssignStatement(self, ctx:CalculadoraParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#ifStatement.
    def enterIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#ifStatement.
    def exitIfStatement(self, ctx:CalculadoraParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#assign.
    def enterAssign(self, ctx:CalculadoraParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#assign.
    def exitAssign(self, ctx:CalculadoraParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#ifStructure.
    def enterIfStructure(self, ctx:CalculadoraParser.IfStructureContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#ifStructure.
    def exitIfStructure(self, ctx:CalculadoraParser.IfStructureContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#compare.
    def enterCompare(self, ctx:CalculadoraParser.CompareContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#compare.
    def exitCompare(self, ctx:CalculadoraParser.CompareContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#relop.
    def enterRelop(self, ctx:CalculadoraParser.RelopContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#relop.
    def exitRelop(self, ctx:CalculadoraParser.RelopContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#codeBlock.
    def enterCodeBlock(self, ctx:CalculadoraParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#codeBlock.
    def exitCodeBlock(self, ctx:CalculadoraParser.CodeBlockContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Parens.
    def enterParens(self, ctx:CalculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Parens.
    def exitParens(self, ctx:CalculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Id.
    def enterId(self, ctx:CalculadoraParser.IdContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Id.
    def exitId(self, ctx:CalculadoraParser.IdContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Int.
    def enterInt(self, ctx:CalculadoraParser.IntContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Int.
    def exitInt(self, ctx:CalculadoraParser.IntContext):
        pass



del CalculadoraParser