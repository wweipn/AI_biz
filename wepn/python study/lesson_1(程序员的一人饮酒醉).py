"""
练习介绍：
在Python的魔法世界，最常用的数据类型有三种：字符串(str)、整数(int)和浮点数(float)。

在数据拼接中，为了将不同的信息进行整合，可以使用拼接符号。但是，如果数据非字符串类型，则无法进行拼接。

此时，我们可以使用数据转换函数str()，将数据转换为字符串类型后，再进行拼接。

题目要求：
请运用所给变量，使用str()函数打印两句话。
第一句话：1人我编程累碎掉的节操满地堆
第二句话：2眼是bug相随我只求今日能早归

其中，变量会在【书写代码】提供，请直接【复制粘贴】：
number1  = 1
number2 = 2
unit1 = '人'
unit2 = '眼'
line1 = '我编程累'
line2 = '是bug相随'
sentence1 = '碎掉的节操满地堆'
sentence2 = '我只求今日能早归'

步骤讲解
1.复制给出的变量，实现变量的赋值
2.使用str()函数
3.使用拼接符号+
4.使用print()函数
"""
number1 = 1
number2 = 2
unit1 = '人'
unit2 = '眼'
line1 = '我编程累'
line2 = '是bug相随'
sentence1 = '碎掉的节操满地堆'
sentence2 = '我只求今日能早归'
print(str(number1) + unit1 + line1 + sentence1 + '\n' + str(number2) + unit2 + line2 + sentence2)