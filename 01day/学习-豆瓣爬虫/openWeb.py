import urllib.request
a = urllib.request.urlopen("http://www.douban.com")
print(a.read().decode('utf-8'))
