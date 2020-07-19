class Teacher:
    face = 'serious'


class Father:
    face = 'sweet'


class Teacher_more(Teacher, Father):
    pass


class Father_more(Father, Teacher):
    pass


time3 = Teacher_more()
time4 = Father_more

print(time3.face)
print(time4.face)
