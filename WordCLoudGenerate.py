import matplotlib.pyplot as plt
from wordcloud import WordCloud
filename = "cut_hole.txt"
f = open(filename, 'r',encoding='utf8')    # 打开文件
data = f.read()
my_wordcloud = WordCloud(font_path="simsun.ttf").generate(data)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
