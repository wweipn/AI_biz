"""
练习目标
这个练习，是建立在上一个练习之上，用代码帮老师完成更多的成绩处理工作。

练习要求
上一个练习中，我们完成了两组成绩的合并和排序。
不过，老师有了新的需求：想知道两组的平均分，以及把低于平均分的成绩也打印出来。
所以，在这个练习中，我们会帮老师计算出两组的平均分，并挑出那些在平均分之下的成绩。
"""
scores1 = [91, 95, 97, 99, 92, 93, 96, 98]
scores2 = []
# # 常规方法
# sum = 0
# for score in scores1:
#     sum = sum + score
#     average = sum / len(scores1)
#     # 上面最好不要去数有几个学生，那样的话，学生数目发生变化就要调代码。
# print('平均成绩是：{}'.format(average))
#
# for score in scores1:
#     if score < average:
#         scores2.append(score)  # 少于平均分的成绩放到新建的空列表中
# print(' 低于平均成绩的有：{}'.format(scores2))  # 上个关卡选做题的知识。

# 请你改造这个代码，用更简洁的方式满足老师的需求。

"""
使用numpy库中的平均方法(average)
"""
import numpy as n

for i in scores1:
    if i < n.average(scores1):
        scores2.append(i)
print('平均分为:{},低于平均分的有:{}'.format(n.average(scores1), scores2))
