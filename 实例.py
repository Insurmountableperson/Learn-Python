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
