# python sqs.py [r1.fastq] [r2.fastq]
import sys

read1 = sys.argv[1]
read2 = read1.replace("1", "2")
sampleName = read1.replace("_1", "")

# with gzip.open(read1, "rb") as r1, gzip.open(
#     read2, "rb"
# ) as r2:

#  sampleName,
#     Bcnt,
#     reads,
#     Npercent,
#     GCpercent,
#     q30percent,
#     q20percent,
#     sampleName,
#     Acnt1 + Acnt2,
#     Tcnt1 + Tcnt2,
#     Gcnt1 + Gcnt2,
#     Ccnt1 + Ccnt2,
#     Ncnt1 + Ncnt2,
#     r1q30 + r2q30,
#     r1q20 + r2q20
def mkStr(read):
    c=0
    l_seq = l_qual = list()
    with open(read, "rb") as r:
        while True:
            for line in r:
                c += 1
                if c % 4 == 2:
                    l_seq.append(line)
                elif c % 4 == 4:
                    l_qual.append(line)
    l_str = [l_seq, l_qual]
    return l_str

def Bcnt(seqs):
    Ncnt = seqs.count('N')
    Acnt = seqs.count('A')
    Tcnt = seqs.count('T')
    Gcnt = seqs.count('G')
    Ccnt = seqs.count('C')
    l_cnt = [Ncnt, Acnt, Tcnt, Gcnt, Ccnt]
    return l_cnt

def qual(l_str):
    q30 = q20 = 0
    s_qual = "".join(l_str[1])
    for k in s_qual:
        if (ord(k) - 33) >= 30:
            q30 += 1
        if (ord(k) - 33) >= 20:
            q20 += 1
