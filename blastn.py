# python blastn.py [scaffoldsFiltered.fasta]
# number of contigs / total contig bases / N50 / Longest / Shortest / Average length
import sys

fileName = sys.argv[1]
with open(fileName, "r") as fr:
    lines = fr.readlines()

l_seq = list()
for i in range(1, len(lines)+1, 2):
    l_seq.append(lines[i].strip())
data=l_seq[1]
# write
fw = open("blast2.txt", "w")
fw.write(data)
fw.close()