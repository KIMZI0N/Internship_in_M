# python NDR.py [Sample1.vcf,Sample2.vcf]
import sys
input = sys.argv[1]
vcf1 = input.split(",")[0]
vcf2 = input.split(",")[1]

fr1 = open(vcf1, "r")
#######################################
s1TotSNP = 0
s2TotSNP = 0
#
s1HetSNP = 0 # 1/0 0/1 1|0 0|1
s2HetSNP = 0
s1HomoSNP = 0 # 1/1 1|1 0/0 0|0
s2HomoSNP = 0
s1ExSNP = 0 # 1
s2ExSNP = 0
#
diffSNP = 0
sameHomoSNP = 0
sameHeteroSNP = 0
########################################
while True: # 헤더 읽기
    line1 = fr1.readline()
    if line1.startswith("#CHROM"):
        break
dic1 = {}
while line1:
    line1 = fr1.readline()
    if "VARTYPE=SNP" in line1: # SNP인 line
        s1TotSNP += 1
        gt1 = line1.split("\t")[-1].split(":")[0]
        alt1 = line1.split("\t")[4]
        pos1 = "{}_{}".format(line1.split("\t")[0], line1.split("\t")[1])

        if (gt1.count("1") == 2):  # s1 1/1 homo
            s1HomoSNP += 1
            s1 = "homo1"
        elif "0" in gt1 and "1" in gt1:  # s1 0/1 1/0 hetero
            s1HetSNP += 1
            s1 = "hetero"
        elif gt1.count("0") == 2: # 0/0 0|0 homo
            s1HomoSNP += 1
            s1 = "homo0"           
        else:
            s1ExSNP += 1 # 1

        if pos1 not in dic1.keys():
            dic1[pos1] = [s1,alt1] # s1은 homo1 또는 homo0 또는 hetero
        else: # 동일한 position이 또 나오면 pass
            pass
    else:
        pass

fr2 = open(vcf2, "r")
while True:
    line2 = fr2.readline()
    if line2.startswith("#CHROM"):
        break
prepos = ""
while line2:
    line2 = fr2.readline()
    if "VARTYPE=SNP" in line2:
        s2TotSNP += 1
        gt2 = line2.split("\t")[-1].split(":")[0]
        alt2 = line2.split("\t")[4]
        if gt2.count("1") == 2:  # s2 1/1 homo
            s2HomoSNP += 1
            s2 = "homo1"
        elif "0" in gt2 and "1" in gt2:  # s2 0/1 1/0 hetero
            s2HetSNP += 1
            s2 = "hetero"
        elif gt2.count("0") == 2: # 0/0 0|0 homo
            s2HomoSNP += 1
            s2 = "homo0"
        else:
            s2ExSNP += 1 # 1

        pos2 = "{}_{}".format(line2.split("\t")[0], line2.split("\t")[1])
        if prepos == pos2: # 직전 position
            continue
        else:
            prepos = pos2
        if pos2 in dic1.keys(): # 샘플2의 line을 차례로 읽다가 샘플1과 같은 position이 있으면 if문으로 들어감.
            if dic1[pos2][0] != s2:      # diff gt
                diffSNP += 1
            else: # dic1[pos2][0] == s2: # same gt
                if dic1[pos2][1] == alt2:            # same alt
                    if s2 == "homo1":
                        sameHomoSNP += 1
                    elif s2 == "hetero":
                        sameHeteroSNP += 1
                    elif s2 == "homo0":
                        diffSNP += 1
                else: # dic1[pos2][1] != alt2        # diff alt
                    if dic1[pos2][0] == s2 == "homo0":
                        sameHomoSNP += 1
                    else:
                        diffSNP += 1
    else:
        pass # not snp

# 중복 position이면 첫번째 line만 비교..! 
# but, NDR계산에 사용되지 않는 변수들에는 포함됨,,
NDR = diffSNP/ (diffSNP + sameHomoSNP + sameHeteroSNP) * 100

print()
print("s1 : {}  |   s2 : {}".format(vcf1, vcf2))
print("------------------------------------------\n\
샘플1의  전체 SNP (InDel제외) 개수: {}\n\
샘플2의  전체 SNP (InDel제외) 개수: {}\n\
------------------------------------------\n\
샘플1 Het SNP의 개수: {}\n\
샘플1 Homo SNP의 개수: {}\n\
샘플1 GT가 예외값인 SNP의 개수: {}\n\
------------------------------------------\n\
샘플2 Het SNP의 개수: {}\n\
샘플2 Homo SNP의 개수: {}\n\
샘플2 GT가 예외값인 SNP의 개수: {}\n\
------------------------------------------\n\
샘플1 과 2의 SNP가 다른 개수: {}\n\
샘플1 과 2의 Het SNP가 같은  개수: {}\n\
샘플1 과 2의 Homo SNP가 같은 개수: {}\n\
------------------------------------------\n\
NDR(Ref Homo 포함): {}".format\
(s1TotSNP, s2TotSNP, s1HetSNP, s1HomoSNP, s1ExSNP, s2HetSNP, s2HomoSNP, \
s2ExSNP, diffSNP, sameHeteroSNP, sameHomoSNP, NDR))
print()
print("{}, {}: ".format(vcf1, vcf2))
if NDR <= 5:
    print("본인, 일란성 쌍둥이")
elif NDR >= 15 and NDR <= 18:
    print("유전학적 형제, 자매 관계")
elif NDR >= 23 and NDR <= 27:
    print("유전학적 부모, 자식 관계")
elif NDR >= 30:
    print("남남")
else:
    print("사잇값") # 사잇값인 경우 NDR값을 보고 결정.
print()