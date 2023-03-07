#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                param=param.swapcase()
                print(param,end="")
                shouldDo=False

            elif format_string[idx] == '#' and format_string[idx+1] == '.' and format_string[idx+3] == 'k':
                param_limit = int(format_string[idx+2])
                param = param.swapcase()
                if len(param) > param_limit:
                    print(param[0:param_limit], end="")
                else:
                    print(param,end="")

                idx=idx+2
                shouldDo=False

            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())