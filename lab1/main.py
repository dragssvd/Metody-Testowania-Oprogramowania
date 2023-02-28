#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                if param.isupper():
                    print(param.lower(),end="")
                else:
                    print(param.upper(),end="")
                shouldDo=False
            else:
                if format_string[idx].isupper():
                    print(format_string[idx].lower(),end="")
                else:
                    print(format_string[idx].upper(),end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
