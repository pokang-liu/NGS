## Introduction
#### This repository contain:
-    Several useful tools in Next Generation Sequencing
-    the code trace of [bwa](https://github.com/lh3/bwa) designed by Li H


## Tools

### flag_check.sh

#### Description:
Do the flag statistics of all the alignment 
it is recommended to used with [samtools](http://www.htslib.org/doc/samtools-1.0.html)

#### input:
 sam/bam file

#### output:
statistics of the flags
#### Usage:
samtools view the samfile.sam | bash ./flag_check.sh > the outputfile.txt

#### sample output:
|||
|-----------|------------|
|163|384939359|
|161|2591826|
|147|385137251|
|...|...|
|...|...|
|...|...|
|bigflag:|30123395564|

     
     

- column1: flag 
- column2: the count of that flag 
- last line: bigflag in dicate the number of flags which are bigger than 256 

### delete_verbose.py

#### Description:
The debug mode (-v 4) in bwa would create several verbose information in output SAM file, this python program could delete those verbose information and output clean SAM file. 
#### input:
 SAM/BAM file with verbose message

#### output:
 SAM/BAM file 
#### Usage:
python delete_verbose.py --In oldfile.out --Out noverbose.sam

### pysam_V2.py

#### Description:
In some case, the same READ would have different read name if they were generated by different aligners wvwn they are identically same, this tool could change them to the same readname.
ps. new read name would be the 3rd field in SAM file (alignment position)
#### input:
 SAM/bam file

#### output:
SAM file with new read name
#### Usage:
python pysam_V2.py --In oldfile.bam --Out newnamefile.sam

#### Sample output file: 


```
@SQ	SN:chr21:8218600-8218800	LN:201
@PG	ID:bwa	PN:bwa	VN:0.7.17-r1188	CL:/home/philippe/bwa_fpga/bwa-0.7.17_dev/bwa mem -v 4 -r 8 /home/philippe/bwa_fpga/data/Whole_chip/Group1_FIFO/DDR8G/NA12878_2reads_INDEL_chr21_g1.fa /home/philippe/bwa_fpga/data/Whole_chip/Group1_FIFO/NA12878_1_2reads_INDEL_chr21_g1.fastq /home/philippe/bwa_fpga/data/Whole_chip/Group1_FIFO/NA12878_2_2reads_INDEL_chr21_g1.fastq
chr21:8218600-8218800	121	chr21:8218600-8218800	44	60	42S59M	=	44	0	CGGGCCGCGCGGGGGCGCCGGGTTTGCCCTCGGATCGCGGCCCCCCCCCCTGCCCCCGCCGGCGGGCCGCCCCCCCCTCCACGCGCCCCGCGCGCGCGGGA	&))&&&&&&)&0&0&&&)&((2((()&50+(8+)&&&)&&&3B<55)&0&&&&@77500&<60B93DDDDDDDDDDBBB:0DDDFHJJHGHHHFFFFFCCC	NM:i:2	MD:Z:5G4T48	AS:i:49	XS:i:0
chr21:8218600-8218801	181	chr21:8218600-8218801	44	0	*	=	44	0	CCCCCCCGCCCCCCCCCAACAACCACAACACACACGCTGTCCCTCGCCTGCCCCTCCCGGGAGGGGGGCGAGAAAAACCACACCAACACCACCCCCAAAAA	0).90&)&&5)&&&&(((&((+((+((+(+())+&(((+&&&&&&&&&&&&&&&','3(('''''''(()))-(.(0((0)))))0)1))))))))+++++	MC:Z:42S59M	AS:i:0	XS:i:0
chr21:8218600-8218802	121	chr21:8218600-8218802	44	60	22S79M	=	44	0	GGGGGGGCCACTGACAAACGTCCCCCCGCCTGTCCCCGCCTGCGGGCCGCCCCCCCCTCCACGCGCCCCGCGCGCGCGGGAGGGCGCGTGCCCCGCCGCGC	&))&((+((++((+(((&)&5&9&&55878<0)0&55)&&&55050&-50)&-5-@8(600B631@56-1350-30-BB?=7;6?<A;<=A;81<DDA=7@	NM:i:1	MD:Z:18G60	AS:i:74	XS:i:0
chr21:8218600-8218803	181	chr21:8218600-8218803	44	0	*	=	44	0	AACCCATATACTAGACATTTATATCAGTAGTAATTTTTCTTACACCTCTTGCTTAATACCCAAATGGCTAGAAGGATTGTGGGGCTCCTCTTTCAAGGTCT	,,((55-((5((5--(6((;36)).)7.).).(().)7)/)=68(.)))4@BB9/0*0)**?:0*1****9:1)*:1+)+)++:+?AA+<D=:2++=++1+	MC:Z:22S79M	AS:i:0	XS:i:0

```


### code trace for [bwa](https://github.com/lh3/bwa)
-    for worker1
-    for worker2
-    the data structure in bwa which store the .ann .amb .fa files 
-    see [wiki](https://github.com/porkbaby/NGS/wiki)
