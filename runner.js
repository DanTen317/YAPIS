const fs = require('fs');

async function runWasm() {
    // 1. Читаем бинарный файл
    const wasmBuffer = fs.readFileSync('./output.wasm');

    // 2. Определяем память (будет переопределена экспортом из wasm)
    let memory;

    // 3. Реализуем импорты (функции, которых не хватает в WASM)
    const importObject = {
        env: {
            // Печать целых чисел
            print_i32: (value) => {
                console.log("[Output Int]:", value);
            },
            // Печать дробных чисел
            print_f32: (value) => {
                console.log("[Output Float]:", value);
            },
            // Печать строк (самое сложное, так как передается указатель)
            print_string: (offset) => {
                const buffer = new Uint8Array(memory.buffer);
                let string = "";
                // Читаем байты, пока не встретим 0 (null-terminator)
                while (buffer[offset] !== 0) {
                    string += String.fromCharCode(buffer[offset]);
                    offset++;
                }
                console.log("[Output String]:", string);
            },
            // Чтение числа (заглушка, так как в nodejs сложно сделать синхронный ввод)
            read_i32: () => {
                return 42; // Возвращаем фейковое число
            },
            print_char: (char_code) => {
                process.stdout.write(String.fromCharCode(char_code));
            },
            // Печать числа без переноса строки
            print_num: (value) => {
                process.stdout.write(value.toString());
            }
        }
    };

    // 4. Инстанцируем модуль
    const wasmModule = await WebAssembly.instantiate(wasmBuffer, importObject);
    const { instance } = wasmModule;

    // 5. Получаем доступ к памяти модуля (чтобы работала print_string)
    memory = instance.exports.memory;

    // 6. Запускаем функцию main
    console.log("--- Starting Program ---");
    instance.exports.main();
    console.log("--- End Program ---");
}

runWasm();