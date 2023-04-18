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

        replace = '#.'
        param_limit = 0
        for idx in range(0,len(format_string)):
            if format_string[idx] == '#' and format_string[idx+1] == '.':
                i=0
                while format_string[idx+2+i].isnumeric():
                    replace = replace + str(format_string[idx+2+i])
                    i+=1
                param_limit = int(format_string[idx+2:idx+2+i])
        
        replace = replace + 'g'

        nparam=''
        if param_limit > len(param):
            for x in range(0, param_limit-len(param)):
                nparam = nparam + '0'
        
        for c in param:
            nparam = nparam + str(convert(int(c)))

        if len(param) > param_limit:
            nparam = nparam[0:param_limit]

        if negative:
            nparam = '-' + nparam
            
        print(format_string.replace(replace, str(nparam)))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())