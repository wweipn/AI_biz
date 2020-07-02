"""
练习目标：
我们会通过今天的项目练习，学习函数的封装和调用。

练习要求：
我们已经有一个hello_kitty抽奖器，现在，请你把这个程序封装成一个新的函数。
"""
# 查看注释，运行代码。
import random
import time


#
# # 用random函数在列表中随机抽奖，列表中只有3位候选者。
#
# luckylist = ['海绵宝宝', '派大星', '章鱼哥']
# # random模块中有个随机选取一个元素的方法：random.choice()。
# a = random.choice(luckylist)  # 从3个人中随机选取1个人。
# print('开奖倒计时', 3)
# time.sleep(1)  # 调用time模块，控制打印内容出现的时间
# print('开奖倒计时', 2)
# time.sleep(1)
# print('开奖倒计时', 1)
# time.sleep(1)
# # 使用三引号打印hellokitty的头像
# image = '''
#  /\_)o<
# |      \\
# | O . O|
#  \_____/
# '''
# print(image)  # ……
# print('恭喜' + a + '中奖！')  # 使用print函数打印幸运者名单

def func(*args):
    """
    *表示接收任意个数量的参数，调用时会将实际参数打包为一个元组传入实参
    :param args:
    :return:
    """
    print(args)

    for i in args:
        print(i)


func('a', 'b', 'c')


def start(*args):
    info()
    print('''
  /\_)o<
 |      \\
 | O . O|
  \_____/
 ''')
    print('恭喜{}获得了奖励'.format(random.choice(args)))



def info():
    n = 3
    for i in range(3):
        print('倒计时开始:{}'.format(n))
        n = n - 1
        time.sleep(1)


start('aa', 'bb', 'cc')
