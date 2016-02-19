#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import lexycs, preprocessor, translate

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(
'''Usage:
{} <source> [binary]

    Whan binary file is missing, output will named "a.kk"'''.format(sys.argv[0]))
        sys.exit(0)
    
    try:
        fp = open(sys.argv[1], 'r')
    except IOError:
        print("{}: can't open file {}".format(sys.argv[0], sys.argv[1]))
        sys.exit(1)
        
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
    
    if (len(sys.argv) == 3):
        fout = sys.argv[2]
    else:
        fout = 'a.kk'
    try:
        fp = open(fout, 'wb')
    except IOError:
        print("{}: can't open file {}".format(sys.argv[0], fout))
        sys.exit(1)
    
    fp.write(code)
    fp.close()
    

main()