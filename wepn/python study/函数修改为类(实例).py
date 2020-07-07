# import math
#
# # 变量key代表循环运行程序的开关
# key = 1
#
#
# # 采集信息的函数
# def myinput():
#     choice = input('请选择计算类型：（1-工时计算，2-人力计算）')
#     if choice == '1':
#         size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
#         number = int(input('请输入人力数量：（请输入整数）'))
#         time = None
#         return size, number, time
#         # 这里返回的数据是一个元组
#     if choice == '2':
#         size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
#         number = None
#         time = float(input('请输入工时数量：（请输入小数）'))
#         return size, number, time
#         # 这里返回的是一个元组
#
#
# # 完成计算的函数
# def estimated(my_input):
#     # 把元组中的数据取出来
#     size = my_input[0]
#     number = my_input[1]
#     time = my_input[2]
#     # 人力计算
#     if (number is None) and (time is not None):
#         number = math.ceil(size * 80 / time)
#         print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size, time, number))
#         # 工时计算
#     elif (number is not None) and (time is None):
#         time = size * 80 / number
#         print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (size, number, time))
#
#     # 询问是否继续的函数
#
#
# def again():
#     # 声明全局变量key，以便修改该变量
#     global key
#     a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
#     if a != 'y':
#         # 如果用户不输入'y'，则把key赋值为0
#         key = 0
#
#     # 主函数
#
#
# def main():
#     print('欢迎使用工作量计算小程序！')
#     while key == 1:
#         my_input = myinput()
#         estimated(my_input)
#         again()
#     print('感谢使用工作量计算小程序！')
#
#
# main()

import math


class Project:

    def __init__(self):
        self.key = 1

    def input(self):
        choice = input('请选择计算类型：（1-工时计算，2-人力计算）')
        if choice == '1':
            self.size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
            self.number = int(input('请输入人力数量：（请输入整数）'))
            self.time = None
        if choice == '2':
            self.size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
            self.number = None
            self.time = float(input('请输入工时数量：（请输入小数）'))

    def estimated(self):
        # 人力计算
        if (self.number is None) and (self.time is not None):
            self.number = math.ceil(self.size * 80 / self.time)
            print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (self.size, self.time, self.number))
            # 工时计算
        elif (self.number is not None) and (self.time is None):
            self.time = self.size * 80 / self.number
            print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (self.size, self.number, self.time))

    def again(self):
        a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
        if a != 'y':
            # 如果用户不输入'y'，则把key赋值为0
            self.key = 0

            # 主函数

    def main(self):
        print('欢迎使用工作量计算小程序！')
        while self.key == 1:
            self.input()
            self.estimated()
            self.again()
        print('感谢使用工作量计算小程序！')


# 创建实例
project1 = Project()
project1.main()