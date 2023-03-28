#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    n = int(param)
    negative = True if n < 0 else False

    if negative:
        n*=-1
        param = str(n)[::-1]
        param=int(param)*-1
    else:
        param = str(n)[::-1]

    print(format_string.replace('#g', str(int(param))))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
