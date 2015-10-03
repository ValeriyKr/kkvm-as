import lexycs, preprocessor, translate

def main():
    fp = open('./src.s', 'r')
    source = []
    for line in fp:
        source.append(line.split())
    fp.close()
    
    data, program = lexycs.analyse(source)
    if program == None:
        return 1
    data, program = preprocessor.pretreat(data, program)
    if program == None:
        return 2
    code = translate.translate(data, program)
    fp = open('./a.out', 'wb')
    fp.write(code)
    fp.close()
    

main()