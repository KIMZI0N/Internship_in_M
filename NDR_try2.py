import sys
vcf1 = sys.argv[1]
vcf2 = sys.argv[2]

fr1 = open(vcf1, "r")
fr2 = open(vcf2, "r")

s1TotSNP = 0
s2TotSNP = 0
s1HetSNP = 0
s2HetSNP = 0
s1HomoSNP = 0
s2HomoSNP = 0
HomoSameSNP = 0
HomoDiffSNP = 0
HetSameSNP = 0
HetDiffSNP = 0

s100SNP = 0
s200SNP = 0

s1NothingSNP = 0
s2NothingSNP = 0
c=0

while True:
    line1 = fr1.readline()
    if line1.startswith("#CHROM"):
        break
while True:
    line2 = fr2.readline()
    if line2.startswith("#CHROM"):
        break
dic1={}
dic2={}

while True:
    line1 = fr1.readline()
    line2 = fr2.readline()
    if "VARTYPE=SNP" in line1:
        s1TotSNP += 1
        gt1 = line1.split("\t")[-1].split(":")[0]
        alt1 = line1.split("\t")[4]
        pos1 = line1.split("\t")[1]
        if gt1.count("1") == 2:  # s1 1/1 homo
            s1HomoSNP += 1
            s1 = "homo"
            dic1[pos1]="{},{}".format(alt1,s1) #############list##############
        elif "0" in gt1 and "1" in gt1:  # s1 0/1 1/0 hetero
            s1HetSNP += 1
            s1 = "hetero"
            dic1[pos1]="{},{}".format(alt1,s1)
        elif gt1.count("0") == 2: # 0/0 0|0
            s100SNP += 1
        else:
            s1NothingSNP += 1

    if "VARTYPE=SNP" in line2:
        s2TotSNP += 1
        gt2 = line2.split("\t")[-1].split(":")[0]
        alt2 = line2.split("\t")[4]
        pos2 = line2.split("\t")[1]
        if gt2.count("1") == 2:  # s2 1/1 homo
            s2HomoSNP += 1
            s2 = "homo"
            dic2[pos2]="{},{}".format(alt2,s2)
        elif "0" in gt2 and "1" in gt2:  # s2 0/1 1/0 hetero
            s2HetSNP += 1
            s2 = "hetero"
            dic2[pos2]="{},{}".format(alt2,s2)
        elif gt2.count("0") == 2: # 0/0 0|0
            s200SNP += 1
        else:
            s2NothingSNP += 1

    if (not line1) and (not line2):
        break
## 샘플마다 딕셔너리 만들고 이중 for문 돌림. -> 런타임 매우매우 김.
for pos1 in dic1.keys():
    for pos2 in dic2.keys():
        if pos1 == pos2:
            # print(dic1[pos1].split(",")[0])
            if dic1[pos1].split(",")[1] == dic2[pos2].split(",")[1] == "homo" and\
                dic1[pos1].split(",")[0] == dic2[pos2].split(",")[0]:
                HomoSameSNP += 1
            elif dic1[pos1].split(",")[1] == dic2[pos2].split(",")[1] == "homo" and\
                dic1[pos1].split(",")[0] != dic2[pos2].split(",")[0]:
                HomoDiffSNP += 1
            elif dic1[pos1].split(",")[1] == dic2[pos2].split(",")[1] == "hetero" and\
                dic1[pos1].split(",")[0] == dic2[pos2].split(",")[0]:
                HetSameSNP += 1
            elif dic1[pos1].split(",")[1] == dic2[pos2].split(",")[1] == "hetero" and\
                dic1[pos1].split(",")[0] != dic2[pos2].split(",")[0]:
                HetDiffSNP += 1

fr1.close()
fr2.close()

NDR = (HetDiffSNP + HomoDiffSNP) / (HetDiffSNP + HetSameSNP + HomoDiffSNP + HomoSameSNP)
print("샘플1의  전체 SNP (InDel제외) 개수: {}\n\
샘플2의  전체 SNP (InDel제외) 개수: {}\n\
샘플1 Het SNP의 개수: {}\n\
샘플1 Homo SNP의 개수: {}\n\
샘플1 0/0 SNP의 개수: {}\n\
샘플1 GT가 예외값인 SNP의 개수: {}\n\
샘플2 Het SNP의 개수: {}\n\
샘플2 Homo SNP의 개수: {}\n\
샘플2 0/0 SNP의 개수: {}\n\
샘플2 GT가 예외값인 SNP의 개수: {}\n\
샘플1 과2의 Het SNP가 다른 개수: {}\n\
샘플1 과2의 Het SNP가 같은  개수: {}\n\
샘플1 과 2의 Homo SNP가 다른 개수: {}\n\
샘플1 과 2의 Homo SNP가 같은 개수: {}\n\
(Het다른개수 + Homo 다른개수)/비교된 전체 SNP의 개수: {}".format\
    (s1TotSNP, s2TotSNP, s1HetSNP, s1HomoSNP, s100SNP, s1NothingSNP, s2HetSNP, s2HomoSNP, \
        s200SNP, s2NothingSNP, HetDiffSNP, HetSameSNP, HomoDiffSNP, HomoSameSNP, NDR))