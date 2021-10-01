# from SAY
with open("scaffoldsFiltered.fasta","r")as f:
    lines= f.readlines()
    NumCont=0
    totalContB=0
    contLen=[]


    for i in lines:
        line = i.strip()
        if line.startswith(">"):
            header = line.split("_")
            totalContB+=int(header[3])
            contLen.append(int(header[3]))
            NumCont+=1
    contLen.sort(reverse=True)
    num=0
    sumLen=0
    for l in contLen:
        sumLen+=int(l)
        if totalContB/2 <= sumLen :
            break
        num+=1
    N50=contLen[num]

AssConF = open("Contigs_Assembly_table","w")
AssConF.write("Contigs_Num\tTotal_base\tN50\tLongest\tShortest\tAverage_Len\n")
AssConF.write("{}\t{}\t{}\t{}\t{}\t{}".format(NumCont,totalContB,N50,contLen[0],contLen[-1],sum(contLen)/len(contLen)))






