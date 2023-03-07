#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    skip = 0
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                param=param.swapcase()
                print(param,end="")
                shouldDo=False

            elif format_string[idx] == '#' and format_string[idx+1] == '.':
                i=0
                while format_string[idx+2+i].isnumeric():
                    i+=1
                
                param_limit = int(format_string[idx+2:idx+2+i])
                param = param.swapcase()
                if len(param) > param_limit:
                    print(param[0:param_limit], end="")
                else:
                    print(param,end="")
                skip = 1+i
                
                shouldDo=False

            else:
                if skip == 0:
                    print(format_string[idx],end="")
                else:
                    skip -= 1
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())