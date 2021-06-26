
# 读取网页内容
# from urllib.request import urlopen
# html = urlopen("http://hnzj.edu.cn")
# print(html.read())

# =========================================
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://baidu.com")
respons = BeautifulSoup(html.read())

print(respons.tbody)  读取网页内容中某个标签

# =========================================

# 异常处理
  # 404 Page Not Found 、500 Internal Server Error
  try：
    html = urlopen("http://www.baidu.com")
  except HTTPError as e:
    print(e)
  else:
    print("网页没有异常")
    
  # 当网页URL错误，或者访问失败时
  if html is None:
    print("网页找不到”）
  else：
    print("URL正常访问")
# =========================================
# 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError  # 在urllib库里找到error模块，只导入一个HttpError函数

def getText(url):  #  构建一个函数
    try:
        html = urlopen(url)
    except HTTPError as e:
        ruturn null
    try:
        respons = BeautifulSoup(html.read())  #  处理
        ObText = respons.body  #  输入body标签的内容
    except AttributeError as e:
        ruturn null
    return ObText

divtext = getText('http://hnzj.edu.cn')
# if title == None:
#     print("找不到网页标题")
# else:
print(divtext)  #  输出
#

# 如爬取电影网
url = "https://www.pianku.li/mv/"
html = urlopen(url)
title = BeautifulSoup(html.read())
title_jie = title.findAll("div",{"class":{"tgr_adr"})  # 读取指定标签
                                 
                                 
