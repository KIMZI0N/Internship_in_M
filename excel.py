# python excel.py [vcf file] [description txt file]
import xlsxwriter, sys

# read vcf
vcf = sys.argv[1]
fr = open(vcf, "r")
l_chr = [] # l_chr = [[l_line0], [l_line1], ...]
for line in fr:
    if line.startswith("#CHROM"):
        header = line
    elif line.startswith("chr"):
        l_line = line.split("\t")
        l_chr.append(l_line)
    else:
        continue

# info
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

# write
vcf = vcf.replace(".","_")
workbook = xlsxwriter.Workbook('{}.xlsx'.format(vcf))
worksheet = workbook.add_worksheet('sheet_a')
Format_Header = workbook.add_format({"font_size": 10, "font_name": "Arial", "align": "center", "valign": "vcenter", "bold": True, "bg_color": "#c4d79b", "text_wrap": True})
Format_Cell_C = workbook.add_format({"font_size": 10, "font_name": "Arial", "align": "center", "valign": "vcenter"})
Format_Cell_L = workbook.add_format({"font_size": 10, "font_name": "Arial", "align": "left", "valign": "vcenter"})

# header
l_header = header.split("\t")
del l_header[7:]
l_header[0] = "CHROM"
l_header.extend(["VARTYPE", "Gene_Name", "GT", "AD_ref", "AD_allele", "DP", "GQ"])
worksheet.write_row(0, 0, l_header, Format_Header)

# chromosome
for i in range(len(l_chr)):
    for j in range(len(l_chr[i])-3):
        worksheet.write(i+1, j, l_chr[i][j], Format_Cell_L)

# VARTYPE, Gene_Name cloumn
v = 1
for k in l_chr_info:
    worksheet.write(v, 7, k["VARTYPE"], Format_Cell_C)
    worksheet.write(v, 8, k["ANN"].split("|")[3], Format_Cell_C)
    v += 1

# format column: GT  AD  DP  GQ
l_chr_form = []
for a in l_chr:
    key = a[-2]
    val = a[-1]
    l_key = key.split(":")
    l_val = val.split(":")
    # print(l_key) # ['GT', 'AD', 'DP', 'GQ', 'PL']
    # print(l_val) # ['1/1', '0,3', '3', '9', '77,9,0\n']
    d_form={}
    for j in range(len(l_key)):
        d_form[l_key[j]] = l_val[j].strip()
    for w in list(d_form.keys()):
        if w == "AD":
            d_form["AD_ref"] = d_form[w].split(",")[0]
            d_form["AD_allele"] = d_form[w].split(",")[1]
    l_chr_form.append(d_form)
# l_chr_form = [{'GT': '1/1', 'AD': '0,3', 'DP': '3', 'GQ': '9', 'PL': '77,9,0', 'AD_ref': '0', 'AD_allele': '3'}, ...]

# write format column
l_form = ['GT', 'AD_ref', 'AD_allele', 'DP', 'GQ']
x = 1
y = 9
for i in range(len(l_chr_form)):
    for j in l_form: #dictionary
        if j in l_chr_form[i].keys():
            worksheet.write(x, y, l_chr_form[i][j], Format_Cell_C)
            y += 1
        elif j not in l_chr_form[i].keys():
            worksheet.write(x, y, "-", Format_Cell_C)
            y += 1
    y = 9
    x += 1

worksheet.autofilter(0,0,x,y+len(l_form)-1)
workbook.use_zip64()
workbook.close()