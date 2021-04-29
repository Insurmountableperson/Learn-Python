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
