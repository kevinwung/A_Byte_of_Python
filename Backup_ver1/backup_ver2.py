import os
import time

#1.需要备份的文件与目录将被指定在一个列表中。
source = ['"C:\\Users\WQQ\PycharmProjects"']
#注意字符串中必须使用双引号用以括起包含空格的名称。

#2.备份文件必须存储在一个主备份目录中
target_dir = 'C:\\Backup'

#如果目标目录还不存在，则需要创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#3.备份文件打包压缩成zip文件
#4.建立由日期构成的子文件夹
today = target_dir + os.sep + time.strftime('%Y%m%d')
#5. zip文件名由当前时间构成
now = time.strftime('%H%M%S')
target =today + os.sep + now + '.zip'  #这段的具体意思还没有理解



if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

#5.使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
print('Zip command is: ')
print(zip_command)
print('Running: ')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup Failed')