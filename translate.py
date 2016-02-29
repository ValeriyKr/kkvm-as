import struct


def make_data_segment(data):
    binary_data = []
    for i, element in enumerate(data, start=1):
        if element[0] == ':word':
            binary_data.append(int(element[1]))
        elif element[0] == ':str':
            for char in element[1]:
                binary_data.append(ord(char))
    print(binary_data)
    return binary_data


def translate(data, program):
    instructions_raw = [
        'fail',
        'nop',
        'push',
        'pop',
        'dup',
        'swap',
        'deep',
        'add',
        'mul',
        'sub',
        'div',
        'inc',
        'dec',
        'shr',
        'shl',
        'ror',
        'rol',
        'bnot',
        'band',
        'bor',
        'bxor',
        'dip',
        'iip',
        'deip',
        'ieip',
        'dnip',
        'inip',
        'writew',
        'readw',
        'writea',
        'reada',
        'deeps',
        'halt',
        'mpeek',
        'mpush',
        'mpop',
        'minc',
        'mdec'
    ]

    data = make_data_segment(data)
    instructions = {}
    for i, instr in enumerate(instructions_raw):
        instructions[instr] = i
    data = [0x6D766B6B] + [len(data)+2] + data
    code = [0 for _ in range(len(data) + len(program) * 3)]
    code[:len(data)] = data

    ip = len(data)
    code[ip] = 0x1
    ip += 1
    for instr in program:
        code[ip] = instructions[instr[0]]
        for arg in instr[1:]:
            ip += 1
            code[ip] = arg
        ip += 1

    ip += 1
    code = code[:ip]
    code = struct.pack('I' * len(code), *code)

    return code
