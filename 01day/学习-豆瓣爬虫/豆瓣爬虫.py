# codeing=utf-8

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影top250.xls"

    saveData(savepath)


#  爬取网页
def getData(baseurl):
    datalist = []
    #  解析数据
    return datalist

#  保存数据
def saveData(savepath):
    print("save....")




if __name__ == "__main__":
    main()