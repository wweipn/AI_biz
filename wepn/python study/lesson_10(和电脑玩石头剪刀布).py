"""
练习目标：
我们会通过今天的作业，做出和电脑进行“石头剪刀布”的游戏。

练习要求：
和电脑玩一个剪刀石头布的游戏：电脑随机出拳，我们可选择出什么。
"""
import random


def guess():
    computer_choice = random.choice(['剪刀', '石头', '布'])
    print(computer_choice)
    my_choice = input('请出拳:')
    if my_choice == computer_choice:
        print('打平了')
    elif (my_choice == '剪刀' and computer_choice == '布') or (my_choice == '石头' and computer_choice == '剪刀') or (
            my_choice == '布' and computer_choice == '石头'):
        print('你赢了')
    else:
        print('你输了')


guess()
