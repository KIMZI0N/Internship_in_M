#!/bin/bash
for var in M {1..22} X Y
do
  less NA12878.vcf | egrep "##|#CHROM|chr$var[[:blank:]]" > chr$var.vcf
done