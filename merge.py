import sys

discription = sys.argv[1]
mg1 = sys.argv[2]
mg2 = sys.argv[3]
mg3 = sys.argv[4]
mg4 = sys.argv[5]

dic = {}
l_num = [] # geneID list
with open(mg1, "r") as fs:
    for line in fs: #line = str
        l_line = line.split("\t") #l_line = list
        l_num.append(l_line[0])

with open(discription, "r") as fr:
    for line in fr:
        l_line = line.strip().split("\t")
        values = [l_line[1],l_line[2],l_line[3],l_line[4]]
        dic[l_line[0]] = "\t".join(values) #dictionary
for k in dic.keys():
    if k not in l_num:
        del(dic[k])

l_result = []
for k in dic.items():
    a="\t".join(k)+"\n"
    l_result.append(a)

i = 0
with open(mg1, "r") as fr1, open(mg2, "r") as fr2, open(mg3, "r") as fr3, open(mg4, "r") as fr4:
    for line1, line2, line3, line4 in zip(fr1, fr2, fr3, fr4):
        l_result[i] = l_result[i].strip()+"\t"+line1.strip()+"\t"+line2.strip().split("\t")[1]+"\t"+line3.strip().split("\t")[1]+"\t"+line4.strip().split("\t")[1]+"\n"
        i += 1

with open("merge.txt","w") as fw:
    fw.write("GeneID\tGene_Symbol\tdescription\tstartPOS\tendPOS\tGeneID\tMG1\tMG2\tMG3\tMG4\n")
    fw.writelines(l_result)



# l_tmp=[]
# for i in range(len(l_tmp)):
#     l_tmp.append("\t".join(dic.items()[i]))
# print(l_tmp)

    # different order!
        # for lineR, lineS in zip(fr, fs): # print(type(lineS))=str
        #     l_lineR = lineR.split("\t")
        #     l_lineS = lineS.split("\t")
        #     print(l_lineR[0])
        #     print(l_lineS[0])
        #     if l_lineR[0] == l_lineS[0]:
        #         fw = open("{}mod.txt","a")
        #         fw.write(lineR)
        #         fw.close()