
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
