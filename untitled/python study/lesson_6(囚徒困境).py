"""
练习目标：
我们会通过今天的作业，综合运用while True循环和 break。

练习要求：
假设有两名囚徒A和B因为合伙犯罪被抓捕，因没有确凿可以指认罪行的证据，审判者准备单独审判两位囚徒。
若两人都认罪，则两人各判10年；若一个认罪一个抵赖，则认罪的人判1年，抵赖的人判20年；若两人都抵赖，则各判3年。

1.开启循环，两人分别选择
首先，我们需要知道两个囚徒各自的选择。
仍有疑惑
用两个input即可。

2.循环当中，有判断和跳出
判决提示：
若两人都认罪，则两人各判10年；
若一个认罪一个抵赖，则认罪的人判1年，抵赖的人判20年；
若两人都抵赖，则各判3年——这种情况下跳出循环。
"""
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
