def analyse(source):
    data_types = [
        ':str',
        ':word'
    ]

    instructions = [
        ('fail', 1),
        ('nop', 1),
        ('push', 2),
        ('pop', 1),
        ('dup', 1),
        ('swap', 1),
        ('deep', 2),
        ('add', 1),
        ('mul', 1),
        ('sub', 1),
        ('div', 1),
        ('inc', 1),
        ('dec', 1),
        ('shr', 2),
        ('shl', 2),
        ('ror', 2),
        ('rol', 2),
        ('bnot', 1),
        ('band', 1),
        ('bor', 1),
        ('bxor', 1),
        # ('dip', 2),
        # ('iip', 2),
        # ('deip', 2),
        # ('ieip', 2),
        # ('dnip', 2),
        # ('inip', 2),
        ('jmp', 2),
        ('jmpe', 2),
        ('jmpn', 2),
        ('writew', 1),
        ('readw', 1),
        ('writea', 1),
        ('reada', 1),
        ('deeps', 1),
        ('halt', 1),
        ('mpeek', 2),
        ('mpush', 2),
        ('mpop', 2),
        ('minc', 2),
        ('mdec', 2)
    ]

    code_segment = -1
    for i, line in enumerate(source, start=1):
        if len(line) == 0:
            continue
        if line[0].startswith(':'):
            if code_segment != -1:
                print('Data in Code Segment: [{0}] in line {1}'.format(line[0], i))
            else:
                if len(line) < 2:
                    print('Elements in Data Segment should be writen as <:type value>, line {0}'.format(i))
                    return None, None
                if line[0] not in data_types:
                    print("Don't know data type [{0}] in line {1}".format(line[0], i))
                    return None, None

                line[1] = ' '.join(line[1:])
                while len(line) != 2:
                    del line[2]
                continue

        if code_segment == -1:
            code_segment = i-1
        if line[0].startswith('.'):
            continue

        if (line[0], len(line)) not in instructions:
            print("Don't know instruction [{0}] with {1} arguments in line {2}".format(line[0], len(line)-1, i))
            return None, None

        if line[0].startswith('jmp'):
            if not line[1].startswith('.'):
                print('Not a label name [{0}] in line {1}'.format(line[1], i))
                return None, None
            else:
                continue

        for arg in range(1, len(line)):
            try:
                line[arg] = int(line[arg])
            except ValueError:
                try:
                    line[arg] = int(line[arg], 16)
                except ValueError:
                    print('Non-integer argument [{0}] in line {1}'.format(line[arg], i))
                    return None, None

    return source[:code_segment], source[code_segment:]

