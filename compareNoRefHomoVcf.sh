#!/bin/bash

ls -v *.vcf > list_noRefHomo.txt # 현 디렉토리에 있는 모든 vcf파일의 목록을 list.txt에 저장.
for i in $(python3.8 mkcombi.py) # mkcombi.py로 조합을 만들어 하나씩 print.
do
    python3.8 NDRnoRefHomo.py $i # 샘플 조합이 하나씩 NDR.py의 input으로 들어감.
done                    # ex) Sample1,Sample2
