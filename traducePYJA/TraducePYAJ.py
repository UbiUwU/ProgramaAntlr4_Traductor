from antlr4 import *
from grammarPyJaLexer import grammarPyJaLexer
from grammarPyJaParser import grammarPyJaParser

class TraducePYAJ(ParseTreeListener):
    
    def __init__(self):
        # Inicialización de listas para el código Java y llamadas a funciones
        self.java_code = ["public class Main {"]
        self.function_calls = []

    # Entrada de la definición de la función
    def enterFunctionDefinition(self, ctx:grammarPyJaParser.FunctionDefinitionContext):
        function_name = ctx.IDENTIFIER().getText()
        params = [f"int {p.getText()}" for p in ctx.parameters().IDENTIFIER()]
        
        # Generar la firma de la función en Java
        self.java_code.append(f"    public static int {function_name}({', '.join(params)}) {{")

    # Salida de la definición de la función
    def exitFunctionDefinition(self, ctx:grammarPyJaParser.FunctionDefinitionContext):
        self.java_code.append("        return resul;")  # Cierre de función
        self.java_code.append("    }")

    # Entrada de la asignación
    def enterAssignment(self, ctx:grammarPyJaParser.AssignmentContext):
        variable = ctx.IDENTIFIER().getText()
        value = ctx.expression().getText()
        
        # Declarar 'int' si es la primera vez que se usa 'resul'
        if variable == "resul":
            self.java_code.append(f"        int {variable} = {value};")
        else:
            self.java_code.append(f"        {variable} = {value};")

    # Entrada de la llamada a función (verifica si la regla es FunctionCall)
    def enterFunctionCall(self, ctx:grammarPyJaParser.FunctionCallContext):
        function_name = ctx.IDENTIFIER().getText()
        arguments = ', '.join(arg.getText() for arg in ctx.arguments().expression())
        function_call = f"{function_name}({arguments})"
        # Añade la impresión del resultado de la función
        self.function_calls.append(f"        System.out.println({function_call});")

    # Método para obtener el código Java generado
    def getJavaCode(self):
        # Agregar el método `main` con las llamadas a función
        main_code = ["    public static void main(String[] args) {"]
        # Añade las llamadas a función si existen; si no, añade una llamada de prueba
        main_code.extend(self.function_calls if self.function_calls else ["        System.out.println(multiplica(5, 6));"])
        main_code.append("    }")
        
        # Combina el código y devuelve como cadena
        return "\n".join(self.java_code + main_code + ["}"])
