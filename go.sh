#!/bin/bash
for i in $(ls *.vcf)
do
	sh chrY.sh $i > $(echo $i | sed "s/.vcf/_result.txt/g")
done
