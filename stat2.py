# number of contigs / total contig bases / N50 / Longest / Shortest / Average length
import sys

fileName = sys.argv[1]
with open(fileName, "r") as fr:
    lines = fr.readlines()

l_seq = list()
for i in range(1, len(lines)+1, 2):
    l_seq.append(lines[i].strip())
seq = "".join(l_seq)
totContig = len(seq) # total contig bases

contigNum = len(l_seq) # number of contigs

contigLen=list()
total = 0
for j in l_seq:
    contigLen.append(len(j))
 
for j in contigLen:
    total += j
    if total >= totContig*0.5:
        N50 = j # N50
        break
# print(contigLen)

# L50 = 0
# for j in contigLen:
#     if j>= N50:
#         L50 += 1
L50 = contigLen.index(N50)+1 # L50

# print
print("number of contigs : {}".format(contigNum))
print("total contig bases : {}".format(totContig))
print("N50 : {}".format(N50)) 
print("L50 : {}".format(L50))
print("Longest : {}".format(contigLen[0])) # Longest
print("Shortest : {}".format(contigLen[-1])) # Shortest
print("Average length : {}".format(sum(contigLen)/len(contigLen))) # Average length