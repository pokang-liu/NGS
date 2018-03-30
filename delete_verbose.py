import numpy as np
import __future__
import re
from argparse import ArgumentParser

parser = ArgumentParser(description='delete_verbose')
parser.add_argument('--In', type=str
                        , default='123')
parser.add_argument('--Out', type=str
    , default='123')
args = parser.parse_args()
fin = open(args.In, "r")
#print ("Name of file: ",args.In)


fout = open(args.Out, "w")
hdr = re.compile("^@[A-Z][A-Z](\t[A-Za-z][A-Za-z0-9]:[ -~]+)+$")
hdr2 = re.compile("^@CO\t.*/")
col_1 = re.compile("[!-?A-~]{1,254}")
col_2 = re.compile("[0,10000000]")
col_3 = re.compile("\*|[!-()+-<>-~][!-~]*")
col_4 = re.compile("[0,10000000]")


while True:
    line = fin.readline()
    if len(line)==0:
        break    
    print ("Read Line: %s" % (line))
    ishdr = hdr.match(line)
    ishdr2 = hdr2.match(line)
    if (ishdr !=None or ishdr2 != None):
        fout.writelines(line)
    
    str_arr=line.split()
    print(len(str_arr))
    if (len(str_arr)<11): 
        continue
    ans1=col_1.match(str_arr[0])
    if(ans1==None):
        continue
    ans2=col_2.match(str_arr[1])
    if(ans2==None):
        continue
    ans3=col_3.match(str_arr[2])
    if(ans3==None):
        continue
    fout.writelines(line)
    print("write:",line)
'''
    else:
        ans1=col_1.match(str_arr[0])
        if(ans1==None):
            continue
        else:    
            ans2=col_2.match(str_arr[1])
            if(ans2==None):
                continue
            else:
                ans3=col_3.match(str_arr[2])
                if(ans3==None):
                    continue
                else:
                    fout.writelines(line)
'''
    
fin.close()   
fout.close()       
    
    