"""
练习目标：
我们会在项目1代码的基础上，添加一个新功能，同时练习循环和判断的知识。

练习要求：
新功能是：每盘（3局）游戏结束后，游戏会问我们是否要继续游戏，再加一盘。
我们可以选择再来一盘，也可以选择退出游戏。

方案1：while True+break
开启一个无限循环，设定跳出条件。

方案2：while 变量名+变量名的布尔值判断
在开头设某变量的布尔值为True，input后开启判断变量的布尔值是否改变。

升级项目1
请你选用上面方案中的一种，为项目1增加“再来一局”的功能。
"""
import time
import random
while 1:
    A_winner = 0
    B_winner = 0
    for i in range(1, 4):
        A_health = 100
        B_health = 100
        print('------------------第{}回合开始------------------'.format(i))
        while A_health > 0 or B_health > 0:
            A_attack = random.randint(10, 30)
            B_attack = random.randint(10, 30)
            if A_health > 0:
                B_health = B_health - A_attack
                print('你发动了攻击,敌人剩余血量:【{}】'.format(B_health, A_health, B_health))
                time.sleep(1.5)
            if B_health > 0:
                A_health = A_health - B_attack
                print('敌人发动了攻击,你剩余血量:【{}】'.format(A_health, A_health, B_health))
                time.sleep(1.5)
            if A_health <= 0 or B_health <= 0:
                if A_health > 0:
                    print('第{}回合,你赢了！！！\n'.format(i))
                    A_winner = A_winner + 1
                    time.sleep(1)
                if B_health > 0:
                    print('第{}回合,你输了！！！\n'.format(i))
                    B_winner = B_winner + 1
                    time.sleep(1)
                break
    if A_winner > B_winner:
        print('你赢了{}个回合,恭喜你获得了胜利\n'.format(A_winner))
    else:
        print('敌人赢了{}个回合,你输了\n'.format(B_winner))
    again = int(input('是否继续游戏?(1:继续,任意键退出)\n'))
    if again == 1:
        continue
    else:
        print('已退出游戏')
        break

