#!/bin/bash
sample=$1
echo $sample
array="ASMTY TSPY IL3RAY SRY TDF ZFY AMGL CSF2RY ANT3Y AZF BPY2 DAZ UTY XGY VCY SNX18P1Y SNX3P1Y CDY PRORY HSFY XKRY PRY"
a="0"
for i in $array
do
    echo "------------------------------------------------"
    s=$(cat ../NA12878.vcf | grep "chrY" | grep "$i" | grep -v "intergenic" | wc -l)
    if [ $s -eq "0" ];then
        cnt=$(cat $sample | grep "chrY" | grep "$i" | grep -v "intergenic" | wc -l)
        if [ $cnt -eq "0" ];then
            echo "$i is not in this sample!"
        elif [ $cnt -ne "0" ];then
            echo "$i is in this sample!"
            echo "count is $cnt"
	        a=`expr $a + 1`
        fi
    fi
done
if [ $a -ne 0 ];then
	echo "$sample is Male!"
else
	echo "$sample is Female!"
fi
