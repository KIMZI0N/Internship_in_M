with open("list.txt", "r") as fr:
    l_vcf = fr.readlines()

c = 0
l_sample = []
for i in range(len(l_vcf)):
    for j in l_vcf[(i + 1):]:
        print("{},{}".format(l_vcf[i].strip(), j.strip()))
