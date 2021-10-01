import sys

read = sys.argv[1]
q=0
l_cnt=list()
with open(read, "r") as f:
    while True:
        line = f.readline()
        l_cnt.append(line)
        if not line: break

del l_cnt[-6:]
fw = open("{}.txt".format(read), "w")
for i in range(len(l_cnt)):
    fw.write(l_cnt[i])
fw.close()
