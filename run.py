import sys
import os
import argparse
import subprocess
from wabt import Wabt
from antlr4 import InputStream, CommonTokenStream

from gen.ListLangLexer import ListLangLexer
from gen.ListLangParser import ListLangParser
from compiler.ast_builder import ASTBuilder
from compiler.compiler import WASMCompiler


def compile_source(source_code):
    try:
        # 1. Лексический и синтаксический анализ
        input_stream = InputStream(source_code)
        lexer = ListLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ListLangParser(stream)
        tree = parser.program()

        if parser.getNumberOfSyntaxErrors() > 0:
            print(f"Syntax Errors found: {parser.getNumberOfSyntaxErrors()}")
            return None

        # 2. Построение AST
        builder = ASTBuilder()
        ast = builder.visit(tree)
        if not ast:
            print("Failed to build AST.")
            return None

        # 3. Компиляция в WAT
        compiler = WASMCompiler()
        wat_code = compiler.compile(ast)
        return wat_code

    except Exception as e:
        print(f"Compilation Error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="ListLang Compiler & Runner")
    parser.add_argument("file", help="Path to the source file (.list)")
    parser.add_argument("--wat", help="Output WAT filename", default="output.wat")
    parser.add_argument("--wasm", help="Output WASM filename", default="output.wasm")
    parser.add_argument("--runner", help="Path to runner.js", default="runner.js")

    args = parser.parse_args()
    source_path = args.file

    # 1. Чтение файла
    if not os.path.exists(source_path):
        print(f"Error: File '{source_path}' not found.")
        sys.exit(1)

    print(f"--- [1/4] Reading {source_path} ---")
    with open(source_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # 2. Компиляция (ListLang -> WAT)
    print(f"--- [2/4] Compiling to WAT ---")
    wat_code = compile_source(code)

    if not wat_code:
        print("Error: Compilation failed.")
        sys.exit(1)

    with open(args.wat, 'w', encoding='utf-8') as f:
        f.write(wat_code)
    print(f"Saved to {args.wat}")

    # 3. Конвертация (WAT -> WASM) с помощью библиотеки wabt
    print(f"--- [3/4] Converting to WASM (via python-wabt) ---")
    try:
        wabt = Wabt()
        # Парсим WAT строку
        # Первый аргумент - имя файла для логов ошибок, второй - содержимое
        wabt.wat_to_wasm(args.wat, args.wasm)

        output = wabt.wasm_validate(args.wasm)
        print(output)
        print(f"Saved to {args.wasm}")

    except Exception as e:
        print(f"Error during WAT->WASM conversion: {e}")
        sys.exit(1)

    # 4. Запуск (Node.js -> runner.js)
    print(f"--- [4/4] Running via Node.js ---")

    if not os.path.exists(args.runner):
        print(f"Error: Runner script '{args.runner}' not found.")
        sys.exit(1)

    try:
        result = subprocess.run(
            ["node", args.runner],
            capture_output=True,
            text=True,
            check=True
        )

        program_output = result.stdout

        print("\n=== PROGRAM OUTPUT ===")
        print(program_output.strip())  # strip чтобы убрать лишние переносы
        print("======================\n")

        output_file = os.path.splitext(source_path)[0] + "_output.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(program_output)

        print(f"Output saved to: {output_file}")

    except subprocess.CalledProcessError as e:
        print("Runtime Error (Node.js):")
        print(e.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()