class Chinese:

    def __init__(self, hometown, region):
        self.hometown = hometown
        self.region = region
        print('程序持续更新中……')
        self.born()
        self.live()

    def born(self):
        print('我生在%s。' % self.hometown)

    def live(self):
        print('我在%s。' % self.region)


wepn = Chinese
wepn('广东', '深圳')
