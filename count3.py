import sys, gzip

read1 = sys.argv[1]
read2 = read1.replace("1", "2")
sampleName = read1.replace("_1", "")

with gzip.open(read1, "rb") as r1, gzip.open(
    read2, "rb"
) as r2:
    lines1 = r1.readlines()
    lines2 = r2.readlines()
 
Acnt1 = Acnt2 = 0
Tcnt1 = Tcnt2 = 0
Gcnt1 = Gcnt2 = 0
Ccnt1 = Ccnt2 = 0
Ncnt1 = Ncnt2 = 0
r1q30 = r2q30 = 0
r1q20 = r2q20 = 0

# sequence string
l_seq1 = list()
for i in range(1, len(lines1), 4):
    l_seq1.append(lines1[i].strip())
seqs1 = "".join(l_seq1)

l_seq2 = list()
for i in range(1, len(lines2), 4):
    l_seq2.append(lines2[i].strip())
seqs2 = "".join(l_seq2)

# quality string
l_qual1 = list()
for i in range(3, len(lines1), 4):
    l_qual1.append(lines1[i])
qual1 = "".join(l_qual1)

l_qual2 = list()
for i in range(3, len(lines2), 4):
    l_qual2.append(lines2[i])
qual2 = "".join(l_qual2) 

# each base count
for k in seqs1:
    if k == "N":
        Ncnt1 += 1
    elif k == "A":
        Acnt1 += 1
    elif k == "T":
        Tcnt1 += 1
    elif k == "G":
        Gcnt1 += 1
    elif k == "C":
        Ccnt1 += 1
    else:
        print(k)

for k in seqs2:
    if k == "N":
        Ncnt2 += 1
    elif k == "A":
        Acnt2 += 1
    elif k == "T":
        Tcnt2 += 1
    elif k == "G":
        Gcnt2 += 1
    elif k == "C":
        Ccnt2 += 1
    else:
        print(k)

# quality
for k in qual1:
    if (ord(k) - 33) >= 30:
        r1q30 += 1
    if (ord(k) - 33) >= 20:
        r1q20 += 1

for k in qual2:
    if (ord(k) - 33) >= 30:
        r2q30 += 1
    if (ord(k) - 33) >= 20:
        r2q20 += 1 
        
# total base counts
Bcnt = len(seqs1) + len(seqs2)

# total read counts
reads = (len(lines1) / 4) + (len(lines2) / 4)

# N%
Npercent = float(Ncnt1 + Ncnt2) / float(Bcnt) * 100
Npercent = round(Npercent,6)
# GC%
GCpercent = float(Gcnt1 + Gcnt2 + Ccnt1 + Ccnt2) / float(Bcnt) * 100
GCpercent = round(GCpercent,2)
# Q30%
q30percent = float(r1q30 + r2q30) / float(Bcnt) * 100
q30percent = round(q30percent,2)
# Q20%
q20percent = float(r1q20 + r2q20) / float(Bcnt) * 100
q20percent = round(q20percent,2)

data = "{}\t{}\t{}\t{}\t{}\t{}\t{}\nSampleName : {}\nTotal A : {}\n\
Total T : {}\nTotal G : {}\nTotal C : {}\nTotal N : {}\n\
Q30 Bases : {}\nQ20 Bases : {}\n".format(
    sampleName,
    Bcnt,
    reads,
    Npercent,
    GCpercent,
    q30percent,
    q20percent,
    sampleName,
    Acnt1 + Acnt2,
    Tcnt1 + Tcnt2,
    Gcnt1 + Gcnt2,
    Ccnt1 + Ccnt2,
    Ncnt1 + Ncnt2,
    r1q30 + r2q30,
    r1q20 + r2q20,
)
 
# write
fw = open("{}.sqs".format(sampleName), "w")
fw.write(data)
fw.close()

