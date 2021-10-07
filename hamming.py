# python hamming.py [TT_Set_A.csv]
import sys
file = sys.argv[1]

# compare string
def strComp(str1, str2):
    l_str1 = l_str2 = []
    l_str1 = str1.split("+")
    l_str2 = str2.split("+")
    ip7 = ip5 = 0
    for a, b in zip(l_str1[0], l_str2[0]):
        if a != b:
            ip7 += 1
    for a, b in zip(l_str1[1], l_str2[1]):
        if a != b:
            ip5 += 1
    return "{}+{}".format(ip7,ip5)

# read TT_Set_A.csv
fr = open(file, "r")
l_base = []
for line in fr:
    if line.startswith("index"):
        continue
    else:
        l_tmp = line.strip().split(",")
        del l_tmp[0], l_tmp[-1]
        base = "+".join(l_tmp)
        l_base.append(base) # l_base->list, 96
fr.close() 

# write .HammingDist.txt
l_ip=[]
fwd = open("TT_Set_A.HammingDist.txt", "w")
fwd.write("IndexSet\t")
for i in range(len(l_base)):
    fwd.write("{}\t".format(l_base[i]))
fwd.write("\n")
for i in l_base:
    fwd.write("{}\t".format(i))
    for j in l_base:
        fwd.write("{}\t".format((strComp(i,j))))
        l_ip.append(strComp(i,j))
    fwd.write("\n")
fwd.close()

# write .HammingDist.freq.txt
d_freq = {} # { "i7+i5" : count, ... }
for ip in l_ip:
    if ip in(list(d_freq.keys())):
        d_freq[ip] += 1
    else:
        d_freq[ip] = 1
fwf = open("TT_Set_A.HammingDist.freq.txt", "w")
fwf.write("HammingDist_i7\tHammingDist_i5\tIndex_Count\n")
l_freq = []
for k, v in(d_freq.items()): # k, v : str, int
    r = k.replace("+","\t")
    r = r + "\t" + str(v) + "\n"
    l_freq.append(r)
fwf.writelines(l_freq)
fwf.close()