#!/usr/bin/env python3

import sys

def convert(number):
    return (number*9+1)%10
    

def my_printf(format_string,param):
    try:
        n = int(param)
        negative = True if n < 0 else False 
    except:
        print(format_string)
    else:
        if negative:
            param = param[1:]
        nparam=''
        for c in param:
            nparam += str((int(c)-1)%10)

        if negative:
            nparam = '-' + nparam
        print(format_string.replace('#g', str(nparam)))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())