a = 1
b = 2
c = 5
d = 10
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# a组合
a_report = 0
for i in list2:
    if a * i == 15:
        print('{}*{} = 15'.format(a, i))
        a_report = a_report + 1
print('{}的组合如上,共有{}种'.format(a, a_report))

# a,b组合
ab_report = 0
for i in list2:
    for n in list2:
        if i * a + n * b == 15:
            print('{}*{} + {}*{}= 15'.format(a, i, b, n))
            ab_report = ab_report + 1
print('{},{}的组合如上,共有{}种'.format(a, b, ab_report))

# a,b,c组合
abc_report = 0
for i in list2:
    for n in list2:
        for v in list2:
            if i * a + n * b + v * c == 15:
                print('{}*{} + {}*{} + {}*{}= 15'.format(a, i, b, n, c, v))
                abc_report = abc_report + 1
print('{},{},{}的组合如上,共有{}种'.format(a, b, c, abc_report))


# b,c组合
bc_report = 0
for i in list2:
    for n in list2:
        if i * b + n * c == 15:
            print('{}*{} + {}*{}= 15'.format(b, i, c, n))
            bc_report = bc_report + 1
print('{},{}的组合如上,共有{}种'.format(b, c, bc_report))

# c组合
c_report = 0
for i in list2:
    if c * i == 15:
        print('{}*{} = 15'.format(c, i))
        c_report = c_report + 1
print('{}的组合如上,共有{}种'.format(c, c_report))

# c,d组合
cd_report = 0
for i in list2:
    for n in list2:
        if i * b + n * c == 15:
            print('{}*{} + {}*{}= 15'.format(c, i, d, n))
            cd_report = cd_report + 1
print('{},{}的组合如上,共有{}种'.format(c, d, cd_report))

# a,d组合
ad_report = 0
for i in list2:
    for n in list2:
        if i * a + n * d == 15:
            print('{}*{} + {}*{}= 15'.format(a, i, d, n))
            ad_report = ad_report + 1
print('{},{}的组合如上,共有{}种'.format(a, d, ad_report))

# a,c组合
ac_report = 0
for i in list2:
    for n in list2:
        if i * a + n * c == 15:
            print('{}*{} + {}*{}= 15'.format(a, i, c, n))
            ac_report = ac_report + 1
print('{},{}的组合如上,共有{}种'.format(a, c, ac_report))

# a,b,d组合
abd_report = 0
for i in list2:
    for n in list2:
        for v in list2:
            if i * a + n * b + v * d == 15:
                print('{}*{} + {}*{} + {}*{}= 15'.format(a, i, b, n, d, v))
                abd_report = abd_report + 1
print('{},{},{}的组合如上,共有{}种'.format(a, b, d, abd_report))


print('所有组合的总和为:{}个'.format(
    a_report + ab_report + ac_report + ad_report + abc_report + bc_report + c_report + cd_report + abd_report))
