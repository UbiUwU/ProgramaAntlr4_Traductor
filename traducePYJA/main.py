import os
from antlr4 import *
from grammarPyJaLexer import grammarPyJaLexer
from grammarPyJaParser import grammarPyJaParser
from TraducePYAJ import TraducePYAJ

def main():
    # Leer el nombre del archivo de entrada (Python) y salida (Texto)
    in_file = input('Nombre del archivo de entrada (Python) > ')
    out_file = input('Nombre del archivo de salida (Texto) > ')

    # Obtener la ruta de la carpeta actual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Ruta completa del archivo de entrada y salida
    in_code_path = os.path.join(current_dir, in_file)
    out_code_path = os.path.join(current_dir, out_file)

    # Leer el archivo Python de entrada
    with open(in_code_path, 'r') as file:
        input_stream = InputStream(file.read())

    # Analizar el código Python con ANTLR
    lexer = grammarPyJaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = grammarPyJaParser(token_stream)
    tree = parser.program()  # Utiliza 'program' como la regla raíz

    # Traducir el árbol de análisis a Java usando el listener
    traduccion_listener = TraducePYAJ()
    walker = ParseTreeWalker()
    walker.walk(traduccion_listener, tree)

    # Obtener el código Java generado
    codigo_java = traduccion_listener.getJavaCode()

    # Guardar el código Java en el archivo de salida
    with open(out_code_path, 'w') as file:
        file.write(codigo_java)

    print(f"Traducción completada. Código Java guardado en: {out_file}")

if __name__ == '__main__':
    main()
