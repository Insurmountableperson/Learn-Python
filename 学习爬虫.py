# 网页请求方法
# from urllib.request import urlopen
# html = urlopen("http://hnzj.edu.cn")
# print(html.read())

# 
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://baidu.com")
respons = BeautifulSoup(html.read())

print(respons.tbody)
