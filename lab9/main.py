#!/usr/bin/env python3

import sys
#  a->j (0->a,1->b, 2->c, 3->d, 4->e,5->f,6->g,7->h, 8->i, 9->j)
def convert(number):
    nparam = ''
    for c in number:
        match c:
            case '0':
                nparam += 'a'
            case '1':
                nparam += 'b'
            case '2':
                nparam += 'c'
            case '3':
                nparam += 'd'
            case '4':
                nparam += 'e'
            case '5':
                nparam += 'f'
            case '6':
                nparam += 'g'
            case '7':
                nparam += 'h'
            case '8':
                nparam += 'i'
            case '9':
                nparam += 'j'   
            case _:
                nparam += c
    return nparam
    
def new_fraction(number):
    nnumber = ''
    for x in number:
        nnumber += str((int(x)+5)%10)
    return nnumber
    
def my_printf(format_string,param):
    try:
        n = float(param)
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
        
        replace = replace + 'h'

        divided = param.split('.')
        
        nparam='' + convert(divided[0])
        
        decimal = '.' + str(new_fraction(str(divided[1])))
        
        if len(decimal) > param_limit:
            decimal = decimal[0:param_limit]
        
        nparam += decimal
        
        if param_limit > len(decimal):
            for x in range(0, param_limit-len(decimal)):
                nparam = nparam + '0'

        if negative:
            nparam = '-' + nparam
            
        print(format_string.replace(replace, str(nparam)))

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())