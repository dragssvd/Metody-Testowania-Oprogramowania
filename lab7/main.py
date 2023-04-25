#!/usr/bin/env python3

import sys

def convert(number):
    nparam = ''
    for c in number:
        match c:
            case 'a':
                nparam += 'g'
            case 'b':
                nparam += 'h'
            case 'c':
                nparam += 'i'
            case 'd':
                nparam += 'j'
            case 'e':
                nparam += 'k'
            case 'f':
                nparam += 'l'
            case _:
                nparam += c
    return nparam

def my_printf(format_string,param):
    print(format_string.replace('#j', convert(str(hex(int(param))).lower().replace('0x',''))))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())