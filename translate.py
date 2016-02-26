import struct


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

    instructions = {}
    for i, instr in enumerate(instructions_raw):
        instructions[instr] = i
    data = [0x6D766B6B] + [2] + data
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
