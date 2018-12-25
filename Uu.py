#!/usr/bin/python3
import re
import sys
import os

str = [];

m_pattern= re.compile(r'(BP_CKE_(\w+)|BP_CK_C_(\w+)|BP_COL(\w\S\w+)|BP_DBI(\w\S\w+)|BP_DM_CB(\w\S\w+)|BP_DQ(\w\S\w+)|BP_ERR_(\w+)|BP_PAR_(\w+)|BP_RDQS_(\w\S\w+)|BP_WDQS_(\w\S\w+)|BP_ROW(\w\S\w+))')

with open("Uu_test.svh",'r') as f:
    for line in f:
        if(m_pattern):
            str = m_pattern.findall(line)
            for i in range(len(str)):
                str[i]=str[i].replace(str[i].upper())
close(f)
