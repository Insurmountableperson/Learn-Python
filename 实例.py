#  判断回文数
shu = input("请输入四位数字：")

date = shu
b1 = int(date[0])
b2 = int(date[1])
b3 = int(date[2])
b4 = int(date[3])

if b1 == b4:
   if b2 != b3:
       print('不是回文数')
   else:
    print('是回文数')
else:
    print('不是回文数')

#  根据身高体重判断BMI值

date1 = float(input('请输入你的身高：(cm)')) / 100
date2 = float(input('请输入你的体重：(kg)'))

bmi = date2 // (date1 * date1)
print('您的bmi值为：', bmi)

if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi <= 23.9:
    print('正常')
elif 24 <= bmi <= 27:
    print('过重')
elif 28 <= bmi <= 32:
    print('肥胖')
elif bmi > 32:
    print('非常肥胖')

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

#  进站
if date == 2:
    if date_num >= 10:
        print('准备进入安检！')
    else:
        print('您还没有买票！请去售票处购买车票！！')


if person %10 == 0:
    print('乘客已经买票，将对其安检')
    if person %5 == 0:
        print('安检合格')
else:
    print('还没购买车票，请去买车票')

    
#  使用for循环输出1+2+3+……+100的结果

sum_an = 0
for i in range(1, 101):
    sum_an += i
    print(sum_an)

 使用while循环输出100以内的偶数
i = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        print(i)


#  使用for循环或者while循环输出100以内的素数

#  for循环

i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if(i%j == 0):
            break
    else:
        print(i)



num = []
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.append(i)
print(num)


#  逢七拍手游戏

for i in range(100):
    if i % 7 == 0 and i != 0 or i % 10 == 7:
        print(i, "拍手")

#  账号登录系统

# passwordError:"用户名或密码错误""您还有几次机会"
# passwordtrue:"登录成功"

""" 单循环体内无法完成此功能
这里次数错可指的是相同账号登录错误次数
passwordbest > 3:"输入错误次数过多,请稍后再试"
"""

#  true
#  user = gao
#  password = 123456


def pd(u, p):
    if u == 'gao' and p == '123456':
        print('登录成功')
    else:
        print("登录失败")
    return 0


c = 3
e = 0
for i in range(c):
    user = input("请输入您的账号：")
    password = input("请输入您的密码：")

    # hc = str(user)  # 缓存user
    if user != "gao" or password != "123456":
        print("您的账号或密码错误")
        i += 1
        print("您还有", c - i, "次机会！")
        # if hc == user:
        #     e += 1
        # if e >= 3:
        #     print("您使用相同账号输错密码超过三次，请稍后再试")
        #     break
    else:
        print("登录成功")
        break

# 九九乘法表

b = input('please input a number:')
for i in range(1,int(b)):       #  左闭右开
    for l in range(1, i+1):
        print(l, '*', i, '=', i*l, end=' ')
    print(' ')


#  正三角形

for i in range(1, 10):
    for kg in range(1, 10-i):
        print(end=' ')
    for x in range(i):
        print('*', end=' ')
    print()



#  好友管理系统

def start_cd():
    print('----------------')
    print('欢迎使用好友管理系统\n','1：添加好友\n','2：删除好友\n','3：备注好友\n','4：展示好友\n','5：退出\n')
    return 0

def user_input(number):
    if number not in ['1','2','3','4','5']:
        print('请输入正确选项!')
    else:
        if number == '1':
            user_addf()
        elif number == '2':
            user_delf()
        elif number == '3':
            user_textf()
        elif number == '4':
            user_showf()
        elif number == '5':
            exit()
    return 0

def user_addf():
    f_name = input('请输入要添加的好友：')
    f_list.append(f_name)
    print('添加好友成功')
    return 0

def user_delf():
    f_name = input('请输入要删除的好友：')
    if f_name in f_list:
       f_list.remove(f_name)
       print('删除好友成功')
    else:
        print("你没有这个好友！")
    return 0

def user_textf():
    f_name = input('请输入要修改的好友的姓名：')
    f_name_after = input('请输入修改后的好友的姓名：')
    if f_name not in f_list:
        print('该好友不存在！')
    else:
        f_list[f_list.index(f_name)] = f_name_after
        print('备注成功')
    return 0

def user_showf():
    if len(f_list) == 0:
        print('好友列表为空')
    for i in f_list:
        print('--------------\n',i, '\t')
    return 0

f_list = []
i = 0
while True:
    start_cd()
    user_input(input('请输入：'))

#  好友通讯录

def jiemian_1():
    print(" ===============\n", '欢迎使用手机通讯录\n', '1.添加联系人\n', '2.查看通讯录\n', '3.删除联系人\n', '4.修改联系人\n', '5.查找联系人\n',
          '6.退出\n', '===============\n')
    return 0

def user_main(user_inputed):
    if user_inputed not in ['1', '2', '3', '4', '5', '6']:
        print('请输入正确的选项！')
    elif user_inputed == '1':  # 添加联系人
        add = {}
        user_add_name = input('请输入联系人的名字：')
        user_add_phone = input('请输入联系人电话：')
        user_add_mail = input('请输入联系人邮箱：')
        user_add_addr = input('请输入联系人的地址：')
        if user_add_name == '' or user_add_phone == '' or user_add_mail == '' or user_add_addr == '':  # 判断输入是否为空
            print('请输入正确信息！')
        else:
            # add.update(姓名=user_add_name,test="test's text")
            add.update(姓名=user_add_name, 电话=user_add_phone, 邮箱=user_add_mail, 地址=user_add_addr)
            user_moreList.append(add)
            user_nameList.append(user_add_name)

    elif user_inputed == '2':  # 查看通讯录
        # print(user_nameList, user_moreList, '\n')
        if len(user_nameList) == 0:
            print('\n通讯录无信息！\n')
        else:
            sw2 = {}
            for i in range(len(user_nameList)):
                print(user_nameList[i],'----------')
                sw2 = user_moreList[i]
                for i2 in sw2.items():
                    print(i2,)

    elif user_inputed == '3':  # 删除联系人
        user_del_input = input('请输入要删除的联系人姓名：')
        if user_del_input == '':
            print('你的输入为空！')
        else:
            if user_del_input not in user_nameList or len(user_nameList) == 0:
                print('该联系人不在通讯录中或通讯录为空')
            for i in range(len(user_nameList)):
                if user_del_input == user_nameList[i]:
                    user_nameList.remove(user_nameList[i])
                    user_moreList.remove(user_moreList[i])
                    print('删除成功')
                    break

    elif user_inputed == '4':  # 修改联系人
        sw = {}
        if len(user_nameList) == 0:
            print('通讯录无信息')
        else:
            user_oldname_input = input('请输入要修改的姓名：')
            if user_oldname_input not in user_nameList or user_oldname_input == '':
                print('通讯录无当前联系人或你内容为空！')
            else:
                user_new_input = input('请输入新的姓名：')
                user_new_phone = input('请输入新手机号：')
                user_new_mail = input('请输入新邮箱：')
                user_new_addr = input('请输入新地址：')
                if user_new_input == '' or user_new_phone == '' or user_new_mail == '' or user_new_addr == '':
                    print('请不要输入空内容！')
                else:
                    for i in range(len(user_nameList)):
                        if user_oldname_input not in user_nameList:
                            print('当前通讯录无该联系人')
                            break
                        if user_oldname_input == user_nameList[i]:
                            user_nameList[i] = user_new_input
                            sw = user_moreList[i]
                            sw.update(姓名=user_new_input, 电话=user_new_phone, 邮箱=user_new_mail, 地址=user_new_addr)
                            user_moreList[i] = sw
                            print('添加成功')
                            break

    elif user_inputed == '5': #  查找联系人
        user_find_name = input('请输入要查找的联系人姓名：')
        if len(user_nameList) == 0:
            print('该通讯录无信息')
        else:
            if user_find_name not in user_nameList:
                print('该联系人不在通讯录中')
            else:
                for i in range(len(user_nameList)):
                    if user_nameList[i] == user_find_name:
                        print(user_nameList[i], user_moreList[i])

    elif user_inputed == '6':
        exit()
    return 0

user_nameList = []
user_moreList = []

while True:
    jiemian_1()
    user_input = input('请输入功能序号：')
    user_main(user_input)
