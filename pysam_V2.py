import pysam 
import numpy as np
import __future__
import xlsxwriter
from multiprocessing import Pool 
from itertools import count, islice
import datetime  
from argparse import ArgumentParser
from collections import Iterator

'''
description:
reference_id is 0 1 2 3....
would map to the name field in the header 
EX: 0-->chr1
    1-->chr2
    ....
    ....
############
after changing the format would look like this...
chr2133028088   16      chr21   33028088        255     50M     read1369        0       0    
GGGATTAATTTAATGCTTGGCTAAATCTTAATTACATATATAATTATCAA      AAAATTAATTTAATGCTTGGCTAAATCTTAATTACATATATAATTATCAA      NM:i:0


'''
def jobs(core_x):
    global line_cnt ,infile_1,cores,outfile_1  
    line_cnt=line_cnt+core_x
    jump_iter = islice(infile_1.fetch(until_eof=True,multiple_iterators=True), core_x, None,cores)

    readstack=np.array([],dtype= np.string_)
    for i in range(6):
        try:
            read1 = jump_iter.next()
        except StopIteration:
            print ('here is end ',i)
            break
        print('core_x',core_x)
        print('infile_1.getrname(read1.reference_id)',infile_1.getrname(read1.reference_id))
        #readname_arr_1 = np.append(readname_arr_1,str(read1.query_name))
        read11 = str(infile_1.getrname(read1.reference_id))+str(read1.reference_start)+'\t'+str(read1.flag)+'\t' \
        +str(infile_1.getrname(read1.reference_id))+'\t'+str(read1.reference_start)+'\t'+str(read1.mapping_quality)  \
        +'\t'+str(read1.cigarstring)+'\t'    \
        +str(read1.query_name)+'\t'+'0'+'\t'+'0'+'\t'+str(read1.query_sequence)+'\t'+str(read1.query_sequence)+'\t'+'NM:i:0'
        
        read_1= np.array(read11,dtype= np.string_)
        read_1 =read_1.reshape((1,))

        #read_1 = np.append(read_1,str(read1.query_name))
        #read_1 = np.append(read_1,str(line_cnt))
    
        #readstack_1  = np.vstack((readstack_1, read_1)) if readstack_1.size else read_1
        readstack  = np.vstack((readstack, read_1)) if readstack.size else read_1        
        #######
        line_cnt=line_cnt+cores
        ###################
        #file1 read.....    realname    line_cnt 
        #file1 read.....    realname    line_cnt

        #...
    return readstack

        
def mycallback(x):  
    #print('newstack\t') 
    for i in range(x.shape[0]):
        print(x[i])
        outfile_1.write(x[i])        
        outfile_1.write('\n')  



        
if __name__ == '__main__': 
    parser = ArgumentParser(description='check')
    parser.add_argument('--In', type=str
                        , default='123')
    parser.add_argument('--Out', type=str
    , default='123')
    args = parser.parse_args()
###########
    line_cnt=1
    #############
    #If template is given, the header is copied from a another AlignmentFile (template must be a AlignmentFile).
    #############
    infile_1 = pysam.AlignmentFile(args.In, "r")
    print('name:',infile_1.get_reference_name(0))
    print('header:',infile_1.text)
    outfile_1 = open(args.Out, "w")  
    outfile_1.write(infile_1.text) 
    #########
    cores = 10 
    e1 = datetime.datetime.now()  
    p = Pool(cores)  
      
    for i in range(cores):  
        p.apply_async(jobs, (i,),callback=mycallback)
    p.close()  
    p.join()  
    
    
    ###############
    infile_1.close()
    outfile_1.close()

    ##############################
    e2 = datetime.datetime.now()  
    print((e2-e1))   
     


