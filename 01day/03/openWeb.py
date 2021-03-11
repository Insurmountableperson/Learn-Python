import urllib.request
a = urllib.request.urlopen("http://www.hnzj.edu.cn")
print(a.read().decode('utf-8'))