# endcoding = utf-8
import io

f = io.open("abc.txt", "wt", encoding = "utf-8") #删除, encoding = "utf-8"这部分运行结果也没有变化，为什么？
f.write(u"这是中文字符串！")
f.close()

text = io.open("abc.txt", encoding = "utf-8").read()
print(text)