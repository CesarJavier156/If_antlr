from antlr4 import *
from .CalculadoraLexer import CalculadoraLexer
from .CalculadoraParser import CalculadoraParser
from .CalculadoraVisitor import CalculadoraVisitor


class EvalVisitor(CalculadoraVisitor):
    def __init__(self):
        self.vars = {}

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[var_name] = value
        return value

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left + right if op == '+' else left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left * right if op == '*' else left / right

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitId(self, ctx):
        name = ctx.ID().getText()
        return self.vars.get(name, 0)

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    # Condicionales
    def visitCompare(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.relop().getText()

        if op == '>': return left > right
        if op == '<': return left < right
        if op == '>=': return left >= right
        if op == '<=': return left <= right
        if op == '==': return left == right
        if op == '!=': return left != right
        return False

    def visitIfStructure(self, ctx):
        condition_value = self.visit(ctx.condition())
        if condition_value:
            self.visit(ctx.block())
        return None


    def visitCodeBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.vars


def ejecutar_calculadora(codigo):
    try:
        input_stream = InputStream(codigo)
        lexer = CalculadoraLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = CalculadoraParser(tokens)
        tree = parser.program()  

        visitor = EvalVisitor()
        visitor.visit(tree)

        salida = f"Código ejecutado:\n{codigo}\n\n Variables finales:\n{visitor.vars}"
        print(salida)
        return salida

    except Exception as e:
        return f"Error: {str(e)}"
