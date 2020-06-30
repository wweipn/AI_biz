"""
练习目标
在这个练习，我们会学会一种新的“格式化字符串”的方法：format()函数。

练习要求
在项目1的末尾，我们学会了一种简化代码的方式：格式化字符串。
不过，还有一种更强大的方法，下面我们会先学习，然后再练习。

format()函数是从 Python2.6 起新增的一种格式化字符串的函数，功能比课堂上提到的方式更强大。
format()函数用来占位的是大括号{}，不用区分类型码（%+类型码）。
具体的语法是：'str.format()'，而不是课堂上提到的'str % ()'。
而且，它对后面数据的引用更灵活，不限次数，也可指定对应关系。
看完右侧的代码、结果和注释，你就懂上面几句话的意思了。
"""
# % 格式化：str % ()
# print('%s%d' % ('数字：', 0))
# print('%d，%d' % (0, 1))
# print('%d，%d，%d' % (0, 1, 0))
#
# name1 = 'Python'
# print('I am learning %s' % name1)  # 注：当只跟一个数据时，%后可不加括号，format()一定要有。
#
# # format()格式化函数：str.format()
# print('\n{}{}'.format('数字：', 0))  # 优势1：不用担心用错类型码。
# print('{}，{}'.format(0, 1))  # 不设置指定位置时，默认按顺序对应。
# print('{1}，{0}'.format(0, 1))  # 优势2：当设置指定位置时，按指定的对应。
# print('{0}，{1}，{0}'.format(0, 1))  # 优势3：可多次调用format后的数据。

print('3.1415926保留小数点后两位:{:.2f}'.format(3.1415926))  # 3.14   保留小数点后两位
print('3.1415926带符号保留小数点后两位:{:+.2f}'.format(3.1415926))  # +3.14    带符号保留小数点后两位
print('-1带符号保留小数点后两位:{:+.2f}'.format(-1))  # -1.00  带符号保留小数点后两位
print('3不带小数:{:.0f}'.format(2.71828))  # 3    不带小数
print('5数字补零:{:0>3d}'.format(5))  # 05    数字补零 (填充左边, 宽度为2)
print('5数字补x (填充右边, 宽度为4):{:x<4d}'.format(5))  # 5xxx	数字补x (填充右边, 宽度为4)
print('10数字补x (填充右边, 宽度为4):{:x<4d}'.format(10))  # 10xx 数字补x (填充右边, 宽度为4)
print('1000000以逗号分隔的数字格式:{:,}'.format(1000000))  # 1,000,000  以逗号分隔的数字格式
print('0.25百分比格式:{:.2%}'.format(0.25))  # 25.00%  百分比格式
print('1000000000指数记法:{:.2e}'.format(1000000000))  # 1.00e+09	指数记法
print('13右对齐 (默认, 宽度为10):{:10d}'.format(13))  # 13    右对齐 (默认, 宽度为10)
print('13左对齐 (宽度为10):{:<10d}'.format(13))  # 13	左对齐 (宽度为10)
print('13中间对齐 (宽度为10):{:^10d}'.format(13))  # 13   中间对齐 (宽度为10)

# name2 = 'Python基础语法'
# print('我正在学{}'.format(name2))  # format()函数也接受通过参数传入数据。
