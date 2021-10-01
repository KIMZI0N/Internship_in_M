import sys

read = sys.argv[1]
stand = sys.argv[2]
dic = {}
l_num = []
with open(stand, "r") as fs: # print(type(s_dic))=list
    for line in fs:#line = str
        l_line = line.split("\t") #l_line = list
        l_num.append(l_line[0])

with open(read, "r") as fr:
    for line in fr:
        l_line = line.strip().split("\t")
        values = [l_line[1],l_line[2],l_line[3],l_line[4]]
        dic[l_line[0]] = "\t".join(values) #dictionary
for k in dic.keys():
    if k not in l_num:
        del(dic[k])
l_keyVal=[]
l_result = []
for k in dic.items():
    a="\t".join(k)+"\n"
    l_result.append(a)

with open("merge.txt","w") as fw:
    fw.writelines(l_result)

# https://data-make.tistory.com/109 [Data Makes Our Future]


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