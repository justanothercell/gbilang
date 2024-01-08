import sys

def parse(program: str) -> str:
    mappings = {
        '<-': '=',
        'do': ':',
        'od': '',
        'then': ':',
        'else': 'else:',
        'fi': ''
    }
    for k, v in mappings.items():
        program = program.replace(k, v)
    return f'def __entry__():\n    ' + program.replace('\n', '\n    ')

def run(program: str) -> any:
    v = {}
    exec(program, v, v)
    return v['__entry__']()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage:')
        print('    py gbilang.py <source.gbi>')
        print('    py gbilang.py <source.gbi> -o <compiled.py>')
        exit()
    file = sys.argv[1]
    with open(file, 'r') as prog:
        source = prog.read()

    program = parse(source)
    if '-o' not in sys.argv:
        result = run(program)
        print(result)
    else:
        dest = sys.argv[sys.argv.index('-o')+1]
        with open(dest, 'w') as prog:
            prog.write(f'{program}\nif __name__ == \'__main__\':\n    result = __entry__()\n    print(result)')
