# python excel_all.py [vcf file]
import xlsxwriter
import sys

# read vcf
vcf = sys.argv[1]
fr = open(vcf, "r")
l_chr = [] # l_chr = [[l_line0], [l_line1], ...]
l_info = []
l_form = []
for line in fr:
    if line.startswith("##INFO"):
        l_info.append(line)
    elif line.startswith("##FORMAT"):
        l_form.append(line)
    elif line.startswith("#CHROM"):
        header = line
    elif line.startswith("chr"):
        l_line = line.split("\t")
        l_chr.append(l_line)
    else:
        continue

# info
l_info_id = []
for i in range(len(l_info)):
    l_tmp = l_info[i].split(",")
    l_info_id.append(l_tmp[0].split("=")[2])

l_chr_info = [] # ['AC=2;AF=1,...' , 'AC=2;AF=1,...' , 'AC=2;AF=1,...' , ...]
for k in l_chr:
    d_info = {}
    l_k = k[7].split(";")
    for l in l_k:
        l_l = l.split("=")
        if len(l_l) == 1:
            d_info[l_l[0]] = l_l[0]
        elif len(l_l) == 2:
            d_info[l_l[0]] = l_l[1]
    l_chr_info.append(d_info)

# format
l_form_id = []
for i in range(len(l_form)):
    l_form_id_split = l_form[i].split("ID=")
    l_form_comma_split = l_form_id_split[1].split(",")
    l_form_id.append(l_form_comma_split[0]) # l_form_id = ['AD', 'DP', 'GQ', 'GT', 'MIN_DP', 'PGT', 'PID', 'PL', 'RGQ', 'SB']

# write
vcf = vcf.replace(".","_")
workbook = xlsxwriter.Workbook('{}_all.xlsx'.format(vcf))
worksheet = workbook.add_worksheet('sheet_a')

# header
l_header = header.split("\t")
del l_header[7:]
form_start_info = len(l_header)
l_header.extend(l_info_id)
l_header[-3] = "Gene_Name"
form_start_pos = len(l_header)
l_header.extend(l_form_id)
for i in range(len(l_header)):
    worksheet.write(0, i, l_header[i])

# chromosome
for i in range(len(l_chr)):
    for j in range(len(l_chr[i])-3):
        worksheet.write(i+1, j, l_chr[i][j])

# info column
# l_chr_info = [{AC:2, AF:1,...} , {AC:2, AF:1,...} , {AC:2, AF:1,...} , ...]
x = 1
y = form_start_info
for i in range(len(l_chr_info)):
    for k in l_info_id: #dictionary
        if k in l_chr_info[i].keys():
            if k == "ANN":
                worksheet.write(x, y, l_chr_info[i][k].split("|")[3])
                y += 1
            else:
                worksheet.write(x, y, l_chr_info[i][k])
                y += 1
        elif k not in l_chr_info[i].keys():
            worksheet.write(x, y, "-")
            y += 1
    y = form_start_info
    x += 1
    # ANN -> GENE_ID
    l_gene_name = []
    for m in l_chr_info[i].keys():
        if m == "ANN":
            l_gene_name.append(l_chr_info[i][m])


# format column
l_chr_form = [] # [{GT:1/1, AD:0,3, ... } , {GT:1/1, AD:0,3, ...} , {GT:1/1, AD:0,3, ...} , ...]
d_form = {}
for a in l_chr:
    key = a[-2]
    val = a[-1]
    l_key = key.split(":")
    l_val = val.split(":")
    # print(l_key) # ['GT', 'AD', 'DP', 'GQ', 'PL']
    # print(l_val) # ['1/1', '0,3', '3', '9', '77,9,0\n']
    # l_form_id = ['AD', 'DP', 'GQ', 'GT', 'MIN_DP', 'PGT', 'PID', 'PL', 'RGQ', 'SB']
    d_form={}
    for j in range(len(l_key)):
        d_form[l_key[j]] = l_val[j].strip()
    l_chr_form.append(d_form)

# write format column
x = 1
y = form_start_pos
for i in range(len(l_chr_form)):
    for j in l_form_id: #dictionary
        if j in l_chr_form[i].keys():
            worksheet.write(x, y, l_chr_form[i][j])
            y += 1
        elif j not in l_chr_form[i].keys():
            worksheet.write(x, y, "-")
            y += 1
    y = form_start_pos
    x += 1
worksheet.autofilter(0,0,x,y+len(l_form_id)-1)
workbook.use_zip64()
workbook.close()