"""
练习目标
这个作业会建立在上一个练习的基础上，完善代码的功能。

练习要求
上一个练习，我们将“囚徒困境”写成了代码，让程序收集两名囚犯的认罪情况，进而决定他们的判决：
两人都认罪，则各判10年；一个认罪一个抵赖，则前者判1年，后者判20年；两人都抵赖，各判3年。只有两人都不认罪，程序才会停止。
现在有一个社会学家，在不同的人群中做这个实验，一旦遇到都不认罪的情况，就停止该人群中的实验。
同时，他希望程序能记录每一对实验者的选择，以及记录第几对实验者都选择不认罪。请你帮帮他吧。
"""
list1 = []
count = 0
while 1:
    A_choice = int(input('囚徒A是否认罪?认罪:0,不认罪:1\n'))
    if A_choice not in (0, 1):
        print('选择错误,重新开始')
        continue
    B_choice = int(input('囚徒B是否认罪?认罪:0,不认罪:1\n'))
    if B_choice not in (0, 1):
        print('选择错误,重新开始')
        continue
    if A_choice == 1 and B_choice == 1:
        print('各判3年')
        break
    elif A_choice == 0 and B_choice == 0:
        print('两人各判10年')
    elif A_choice != B_choice:
        if A_choice == 1:
            print('囚犯A判20年,囚犯B判1年')
        elif B_choice == 1:
            print('囚犯A判1年,囚犯B判20年')
    count = count + 1
    list1.append({'批次': count, 'A': A_choice, 'B': B_choice})
print(list1)
