"""
练习目标：
通过今天的练习，运用课堂上学到的知识：如何给代码debug，慢慢培养debug的习惯和信心。

练习要求：
找出下列3个代码的错误，并将其纠正。
"""
# 第一种
# scores = {'语文': 89, '数学': 95, '英语': 80}
#
#
# def get_average(scores):
#     sum_score = 0  # sum_score 作为函数内部的局部变量，从而可以为函数所用。
#     for subject, score in scores.items():
#         sum_score += score
#     print('现在的总分是%d' % sum_score)
#     ave_score = sum_score / len(scores)
#     print('平均分是%d' % ave_score)
#
#
# get_average(scores)


# 第二种
not_bad_word = True
while not_bad_word:
    x = input('请给旺财取个外号：')
    if x == '小狗' or x == '汪汪':
        print('我生气了，不想理你了！')
        not_bad_word = False
print('对不起，以后我不会这么叫你了')
