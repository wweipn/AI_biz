"""
练习目标：
我们会通过今天的作业，再次运用在课堂上学过的关于类的基础知识。

练习要求：
请用今天学到的知识创建一个机器人，让其具备以下功能：
一是会让你给ta 起名，也会问你的名字，然后跟你打招呼（如“你好，吴枫。我是瓦力。遇见你，真好。”）；
二是会让你说一个愿望，然后帮你重复三次（因为 ta 觉得重要）。
"""


class Boot:
    def __init__(self):
        self.name = input('给我起个名字吧!\n')
        self.master = input('对了,我要怎么称呼你呢?\n')
        print('{}你好,我叫{},很高兴认识你\n'.format(self.master, self.name))

    def wish(self):
        text = input('你的愿望是什么呢?\n')
        for i in range(3):
            print('{}的愿望是{}'.format(self.master, text))


wepn_boot = Boot()

wepn_boot.wish()
