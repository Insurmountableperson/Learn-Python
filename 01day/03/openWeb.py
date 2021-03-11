import urllib.request
a = urllib.request.urlopen("http://www.baidu.com")
print(a.read().decode('utf-8'))
