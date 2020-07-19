class Student:
    def __init__(self, name, job=None, time=0.00, time_effective=0.00):
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective

    def count_time(self, hour, rate):
        self.time += hour
        self.time_effective += hour * rate


class Programmer(Student):
    def __init__(self, name):
        Student.__init__(self, name, job='programmer', time=0.00, time_effective=0.00)

    def count_time(self, hour, rate=1):
        Student.count_time(self, hour, rate)


student1 = Student('韩梅梅')
student2 = Programmer('李雷')
print(student1.job)
print(student2.job)
student1.count_time(10, 0.8)
student2.count_time(10)
print(student1.time_effective)
print(student2.time_effective)
