#  判断回文数
# shu = input("请输入四位数字：")
#
# date = shu
# b1 = int(date[0])
# b2 = int(date[1])
# b3 = int(date[2])
# b4 = int(date[3])
#
# if b1 == b4:
#    if b2 != b3:
#        print('不是回文数')
#    else:
#     print('是回文数')
# else:
#     print('不是回文数')

#  根据身高体重判断BMI值

# date1 = float(input('请输入你的身高：(cm)')) / 100
# date2 = float(input('请输入你的体重：(kg)'))
#
# bmi = date2 // (date1 * date1)
# print('您的bmi值为：', bmi)
#
# if bmi < 18.5:
#     print('过轻')
# elif 18.5 <= bmi <= 23.9:
#     print('正常')
# elif 24 <= bmi <= 27:
#     print('过重')
# elif 28 <= bmi <= 32:
#     print('肥胖')
# elif bmi > 32:
#     print('非常肥胖')

#  模拟乘客进站流程
from typing import Set

print("欢迎进入车站！\n 请选择：\n ===============")
print("1:购票  2:进站  3：离开 \n")

key = [0, 0,]


def cd():
    print("1:购票  2:进站  3：离开 \n")
    return 0

def buyP(i=''):
    i = 1
    print('购票成功')
    return i


def aj():
    i = 1
    print('安检完成！')
    return i


def ajErrot():
    i = 'E'
    print('安检不通过')
    return i


for a in range(10):
    date = int(input('请输入序号：'))
    if date == 1:
        key[0] = buyP()
        # print(key)
    elif date == 2:
        if key[0] == 1:
            print('检测到你的车票，准备安检')

           key[1] = aj()
        if key[1] == 1:
            quit(print('您已经成功进站！'))
        else:
            print('进站失败')
        else:
            print('请去购买车票')
    elif date == 3:
        quit(print('您已离开'))

# #  进站
# if date == 2:
#     if date_num >= 10:
#         print('准备进入安检！')
#     else:
#         print('您还没有买票！请去售票处购买车票！！')
#
#


# if person %10 == 0:
#     print('乘客已经买票，将对其安检')
#     if person %5 == 0:
#         print('安检合格')
# else:
#     print('还没购买车票，请去买车票')
#
    
    
    
    
    
    
    
#  使用for循环输出1+2+3+……+100的结果

# sum_an = 0
# for i in range(1, 101):
#     sum_an += i
#     print(sum_an)

#  使用while循环输出100以内的偶数
# i = 0
# while i <= 100:
#     i += 1
#     if i % 2 == 0:
#         print(i)


#  使用for循环或者while循环输出100以内的素数

#  for循环

# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if(i%j == 0):
#             break
#     else:
#         print(i)
#


# num = []
# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         num.append(i)
# print(num)


#  逢七拍手游戏

# for i in range(100):
#     if i % 7 == 0 and i != 0 or i % 10 == 7:
#         print(i, "拍手")

#  账号登录系统
# passwordError:"用户名或密码错误""您还有几次机会"
# passwordtrue:"登录成功"

""" 单循环体内无法完成此功能
这里次数错可指的是相同账号登录错误次数
passwordbest > 3:"输入错误次数过多,请稍后再试"
"""

#  true
#   user = gao
#   password = 123456


# def pd(u, p):
#     if u == 'gao' and p == '123456':
#         print('登录成功')
#     else:
#         print("登录失败")
#     return 0
#
#
# c = 3
# e = 0
# for i in range(c):
#     user = input("请输入您的账号：")
#     password = input("请输入您的密码：")
#
#     # hc = str(user)  # 缓存user
#     if user != "gao" or password != "123456":
#         print("您的账号或密码错误")
#         i += 1
#         print("您还有", c - i, "次机会！")
#         # if hc == user:
#         #     e += 1
#         # if e >= 3:
#         #     print("您使用相同账号输错密码超过三次，请稍后再试")
#         #     break
#     else:
#         print("登录成功")
#         break

# 九九乘法表

# b = input('please input a number:')
# for i in range(1,int(b)):       #  左闭右开
#     for l in range(1, i+1):
#         print(l, '*', i, '=', i*l, end=' ')
#     print(' ')
#

#  正三角形
#
# for i in range(1, 10):
#     for kg in range(1, 10-i):
#         print(end=' ')
#     for x in range(i):
#         print('*', end=' ')
#     print()
#




