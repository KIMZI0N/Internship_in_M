#!/bin/bash
for i in $(ls /data/SampleData/hWGS/NDR_dataset/*.vcf | rev | cut -d "/" -f1 | rev | sed "s/vcf/_result.txt/g")
do
        echo $i
done
