import jieba
import re
input_filename = "hole.txt"
output_filename = "cut_hole.txt"
wordlist =""
f = open(input_filename, 'r',encoding='utf8')    # 打开文件
lines = f.readlines() #a list
for line in lines:
    line = re.sub(r'\[.*\]','',line)#替换掉[XXX]
    line = re.sub(r'Re.*:','',line)
    line = re.sub(r'[《》，。！？；：“”{}~+-=（）【】……]','',line)
    line = line.strip()
    seg_list = jieba.cut(line,cut_all=False)
    wordlist = wordlist+" ".join(seg_list)
#print(wordlist)
with open(output_filename,"w",encoding='UTF-8') as f:
    f.write(wordlist)



