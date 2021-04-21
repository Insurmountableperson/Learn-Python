v1.0

#  产生随机数，random的随机种子由系统时间生成
import random

#  进度条
#  import time
#   for i in range(10):
#     time.sleep(0.3) # 此行必须添加，否则可能看到的直接是最后一行，可能是因为cpu速度快？
#     print('\r updating the line of ....%d' % i, end="")
#

# 生成随机数函数
def keyNum():
    key = []
    for i in range(8):
        key.append(random.randint(0, 4))

    # print(key)
    return key


#  抽奖区域界面
def gglJm():
    print()
    print()
    print('---------产生了一张刮刮乐---------')
    print()
    print('-------------------------------')
    print('|  区域1   |   区域2   |  区域3  |')
    print('-------------------------------')
    print('|  区域4   |   区域5   |  区域6  |')
    print('-------------------------------')
    print('|  区域7   |   区域8   |  刷新0  |')
    print('-------------------------------')
    return 0


#  程序菜单
def userCome():
    key = 0
    print('---------------------')
    print('|   1  开始游戏      |')
    print('---------------------')
    print('|   2  退出游戏      |')
    print('---------------------')
    print('游戏不正确操作会导致程序退出！')
    userdata = input('请选择：')

    if userdata.isdigit() is not False:
        if 0 < int(userdata) < 3:
            userdataInt = int(userdata)
        else:
            print('由于你不正确操作，程序退出！')
            exit()
    else:
        print('由于你不正确操作，程序退出！')
        exit()
    return userdataInt


#  奖项内容
jieguo = list(['谢谢惠顾','一等奖','二等奖','三等奖'])

#  main


Server_main = 1
while Server_main == 1:
    keyTrue = keyNum()  # 调用随机函数，赋值给（刮奖可能性）key
    userC = userCome()  # 函数返回值到userC（user choose）
    #  判断用户的输入
    if userC == 1:  # 选择序号1
        gglJm()
        userCJNumber = input('请输入要刮奖的区域：')
        if userCJNumber.isdigit() is not False:  # 利用isdigit()方法，判断输入是否为数值

            if int(userCJNumber) >= 9:
                print()
                print('请遵守游戏规则，正确选择区域！')
            else:
                userCJNumber_Int = int(userCJNumber)
                if userCJNumber_Int == 0:
                        for i in range(1):
                            keyTrue = keyNum()  # 调用随机函数，赋值给（刮奖可能性）key
                            print('结果刷新完成')
                            break
                else:
                    endjieguo = keyTrue[userCJNumber_Int]
                    print('\n---------------------\n'+'你所刮奖的结果是：',jieguo[endjieguo-1]+'\n---------------------\n')
                    continue
        else:
            print()
            print('请输入数字！')
            break
    elif userC == 2:
        print()
        print('程序退出')
        exit()







#  测试无限循环运行条件
# i = 1
# while i == 1:
#     print('test')
#     s = input('改变循环key：')
#     i = int(s)        #  可通过在循环体内改变条件变量的值
