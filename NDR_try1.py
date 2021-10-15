import sys
vcf1 = sys.argv[1]
vcf2 = sys.argv[2]

### variable ##
s1TotSNP = 0
s2TotSNP = 0
s1HetSNP = 0
s2HetSNP = 0
s1HomoSNP = 0
s2HomoSNP = 0
s1HetDiffSNP = 0
s2HetDiffSNP = 0
s1HetSameSNP = 0
s2HetSameSNP = 0
s1HomoDiffSNP = 0
s2HomoDiffSNP = 0
s1HomoSameSNP = 0
s2HomoSameSNP = 0

HomoSameSNP = 0
HomoDiffSNP = 0
HetSameSNP = 0
HetDiffSNP = 0
c = 0
with open(vcf1, "r") as fr1, open(vcf2, "r") as fr2:
    # header
    while True:
        line1 = fr1.readline()
        if line1.startswith("#CHROM"):
            break
    while True:
        line2 = fr2.readline()
        if line2.startswith("#CHROM"):
            break
    # chromosome
    while True:
        line1 = fr1.readline()
        line2 = fr2.readline()
        if "VARTYPE=SNP" in line1:
            s1TotSNP += 1
            s1 = "snp" 
        else:
            pass
        if "VARTYPE=SNP" in line2:
            s2TotSNP += 1
            s2 = "snp"
        else:
            pass
        ############# same position and snp ################
        while line1 and line2:
            pos1 = line1.split("\t")[1]
            pos2 = line2.split("\t")[1]
            if pos1 == pos2:
                position = "same"
                break
            elif int(pos1) > int(pos2):
                line2 = fr2.readline()
                if "VARTYPE=SNP" in line2:
                    s2TotSNP += 1
                else:
                    pass
                continue
            elif int(pos1) < int(pos2):
                line1 = fr1.readline()
                if "VARTYPE=SNP" in line1:
                    s1TotSNP += 1
                else:
                    pass
                continue
            else:
                pass
        if s1 == "snp" and s2 == "snp" and position == "same":
            tmp1 = line1
            tmp2 = line2
        else:
            pass
        ####### gt and alt ##############        
        if tmp1 and tmp2:
            gt1 = tmp1.split("\t")[-1].split(":")[0]
            alt1 = tmp1.split("\t")[4]
            gt2 = tmp2.split("\t")[-1].split(":")[0]
            alt2 = tmp2.split("\t")[4]
            if "1/1" in gt1:  # 1/1 homo
                s1HomoSNP += 1
                s1 = "homo"
            elif "0" in gt1 and "1" in gt1:  # 0/1 1/0 hetero
                s1HetSNP += 1
                s1 = "hetero"
            
            else:
                print("else1")
                break
            if "1/1" in gt2:  # 1/1 homo
                s2HomoSNP += 1
                if s1 == "homo" and alt1 == alt2:  # s2, homo, same
                    HomoSameSNP += 1
                    continue
                elif s1 == "homo" and alt1 != alt2:
                    HomoDiffSNP += 1
                    continue
            elif "0" in gt2 and "1" in gt2:  # 0/1 1/0 hetero
                s2HetSNP += 1
                if s1 == "hetero" and alt1 == alt2:  # s2, hetero, same
                    HetSameSNP += 1
                    continue
                elif s1 == "hetero" and alt1 != alt2:
                    HetDiffSNP += 1
                    continue
            else:
                print("else2")
                break

            
        if (not line1) or (not line2):
            break 
print(s1TotSNP,s2TotSNP)
# HetDiffSNP #= (s1HetDiffSNP + s2HetDiffSNP)/2
# HetSameSNP #= (s1HetSameSNP + s2HetSameSNP)/2
# HomoDiffSNP #= (s1HomoDiffSNP + s2HomoDiffSNP)/2
# HomoSameSNP #= (s1HomoSameSNP + s2HomoSameSNP)/2

# percent = (HetDiffSNP + HomoDiffSNP) / s1TotSNP
# print("샘플1의  전체 SNP (InDel제외) 개수: {}\n\
# 샘플2의  전체 SNP (InDel제외) 개수: {}\n\
# 샘플1 Het SNP의 개수: {}\n\
# 샘플1 Homo SNP의 개수: {}\n\
# 샘플2 Het SNP의 개수: {}\n\
# 샘플2 Homo SNP의 개수: {}\n\
# 샘플1 과2의 Het SNP가 다른 개수: {}\n\
# 샘플1 과2의 Het SNP가 같은  개수: {}\n\
# 샘플1 과 2의 Homo SNP가 다른 개수: {}\n\
# 샘플1 과 2의 Homo SNP가 같은 개수: {}\n\
# (Het다른개수 + Homo 다른개수)/비교된 전체 SNP의 개수: {}".format\
#     (s1TotSNP, s2TotSNP, s1HetSNP, s1HomoSNP, s2HetSNP, s2HomoSNP, \
#         HetDiffSNP, HetSameSNP, HomoDiffSNP, HomoSameSNP, percent))