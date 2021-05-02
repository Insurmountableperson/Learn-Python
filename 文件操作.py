#  打开文件
#  文件名，打开模式，编码格式
open(filename,mode='r',encoding=none)   

#  常用打开模式
#  r：以只读方式打开文件（默认）
#  w：以只写的方式打开文件
#  a: 以追加的方式打开文件

#  example01
txt_data = open（'filename.txt','r') #  使用open()函数以只读方式打开文件

#  关闭文件
txt_data.close()

#  文件读取
#  size为文件读取长度，缺省为读取全部

#  字符读取
txt_data.read([size])

#  行读取
txt_data.readline()

#  整体读取,并返回列表
txt_data.readlines()

#  文件写入,成功则返回长度
txt_data.write(str)
#  行写入
txt_data.writelines([str])

#  example02
txt_data = open('filename',mode = 'a+')
print(txt_data.write('hello world')
#  example03
txt_data = open('filename',mode = 'a+')
print(txt_data.writeline(['\n'+'python','程序开发'])

#  获目录的文件列表
listdir(path)

#  example04
import os
current_path = r"D:\\"
print(os.listdir(current_path))


----------------------
f = open('centos.txt')
a = open('centos2.txt',"w")
in_text = f.readlines()
i = 1
for tt in in_text:
    print(tt,a.write(tt))   ##  此处输出时会返回字符长度

f.close()
a.close()

import os
os.rename('centos.txt','centos11.txt')
