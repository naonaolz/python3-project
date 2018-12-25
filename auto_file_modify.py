#!/usr/bin/python3

import re

with open('a.txt','r') as f, open('a.vh','a+') as f1:
    for line in f:
        line = re.sub('\n','',line)
        print(line)
        if re.search(r'INIT(.*)',line)!=None:
            print(type(line))
            (str0,str1)=line.split(',')
            addr_num=str0.split('\'h')[1]
            data_num=str1.split('\'h')[1]
            print(addr_num)
            print(data_num)
            f1.write('write_reg("CSR_ADR",0x'+addr_num+'u);\n'+'write_reg("CSR_CMD", 0x'+data_num+'u);\n')
        else:
            f1.write(line+'\n')
f1.close();
f.close();
