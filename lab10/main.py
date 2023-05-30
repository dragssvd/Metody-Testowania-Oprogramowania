#!/usr/bin/env python3

import sys
    
def new_param(number):
    return int((number*2)/len(str(number)))
    
def my_printf(format_string,param):
    try:
        n = int(param)
        negative = True if n < 0 else False 
    except:
        print(format_string)
    else:
        if negative:
            param = param[1:]

        replace = '#a'

        nparam = new_param(int(param))
        if nparam%2 != 0:
            nparam = str(hex(nparam)).replace('0x', '')
            
        if negative:
            nparam = '-' + str(nparam)
            
        print(format_string.replace(replace, str(nparam)))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())