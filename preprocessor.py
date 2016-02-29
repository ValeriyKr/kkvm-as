def pretreat(data, source):
    for line, element in enumerate(data, start=1):
        if element[0] == ':word':
            try:
                int(element[1])
            except ValueError:
                print('Non-integer value given for {0} type in line {1}'.format(element[0], line))
                return None, None

    # Labels and jumping processing
    labels = {}
    offset = 0
    for line, instr in enumerate(source, start=1):  # TODO: right first line index
        if instr[0].startswith('.'):
            if instr[0] in labels:
                print('Non-unique label name [{0}] in line {1}'.format(instr[0], line))
                return None, None

            labels[instr[0]] = offset
            instr[0] = 'nop'
        offset += len(instr)

    offset = 0
    dip = {'jmp': 'dip', 'jmpe': 'deip', 'jmpn': 'dnip'}
    iip = {'jmp': 'iip', 'jmpe': 'ieip', 'jmpn': 'inip'}
    for line, instr in enumerate(source, start=1):  # TODO: right first line indexs
        if instr[0].startswith('jmp'):
            if instr[1] not in labels:
                print('No label called [{0}] in line {1}'.format(instr[1], line))
                return None, None
            instr[1] = labels[instr[1]] - offset
            if instr[1] < 0:
                instr[0] = dip[instr[0]]
                instr[1] = -instr[1]
            else:
                instr[0] = iip[instr[0]]

        offset += len(instr)

    return data, source
