poem = '''Programming is fun
When the work is done
if you wanna make your work also fun:          
use Python!'''

#打印文件以编辑（'w'riting）
f = open('poem.txt', 'w')
#向文件中编写文件
f.write(poem)
#关闭文件
f.close()
#如果没有特别指定，将假定启用默认的阅读（'r'ead）模式
f = open('poem.txt')
while True:
    line = f.readline()
    #零长度指示EOF
    if len(line) == 0:
        break
        #每行（'line'）的末尾都已经有了换行符，因为它是从一个文件中读取的
    print(line, end = '')

f.close()
