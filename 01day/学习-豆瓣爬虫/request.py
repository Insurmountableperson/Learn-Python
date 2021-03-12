import urllib.request
import urllib.parse

#  post
#
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#  get
# response = urllib.request.urlopen("http://httpbin.org/get",timeout=1) #1秒的延迟
# print(response.read().decode("utf-8"))
#  异常捕获

# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)  # 1秒的延迟
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

#  简单解析
# response = urllib.request.urlopen("http://baidu.com")
# print(response.getheader("Server"))

#  解决防爬虫

# url = "http://www.douban.com"
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
# headers = {
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.48"
# }
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

