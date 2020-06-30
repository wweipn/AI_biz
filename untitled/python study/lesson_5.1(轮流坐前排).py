"""
练习目标
通过这个练习，你会尝试用循环来解决生活中的问题，并了解一种新的列表方法。

练习要求
小明、小红、小刚是同班同学，且坐在同一排，分别坐在第一位、第二位、第三位。
由于他们的身高都差不多，所以，老师计划让他们三个轮流坐在第一位。
每次换座位的时候，第一位变第三位，后面两位都往前一位。
"""
# 增\删方式实现
students = ['小明', '小红', '小刚']
for i in range(3):
    students.append(students[0])
    del students[0]
    print(students)

# 使用pop函数实现
for i in range(3):
    students.append(students.pop(0))  # 运用pop()函数，同时完成提取和删除,并将移除的student1安排到最后一个座位。
    print(students)
