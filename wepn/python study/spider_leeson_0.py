import requests

# # res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# # # 获取响应状态码
# # print(res.status_code)
#
# res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# # 发出请求，并把返回的结果放在变量res中
# pic = res.content
# # 把Reponse对象的内容以二进制数据的形式返回
# photo = open('D:/Users/Wepn/PycharmProjects/wepn/python study/ppt.jpg', 'wb')
# # 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# # 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
# photo.write(pic)
# # 获取pic的二进制内容
# photo.close()
# # 关闭文件
#
# res1 = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# # 下载《三国演义》第一回，我们得到一个对象，它被命名为res
# novel = res1.text
# # 把Response对象的内容以字符串的形式返回
# sanguo = open('D:/Users/Wepn/PycharmProjects/wepn/python study/《三国演义》.txt', 'a+')
# sanguo.write(novel)
# sanguo.close()


"""
作业1
"""

source1 = requests.get('https://localprod.pandateacher.com/python-manuscript'
                       '/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')

sources_text = source1.text
print(sources_text)


"""
作业2
"""

source2 = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')

photo1 = source2.content

a = open('D:/Users/Wepn/PycharmProjects/wepn/python study/test.jpg', 'wb')

a.write(photo1)
a.close()


"""
作业3
"""

source3 = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

test_mp3 = source3.content

test_mp3_file = open('D:/Users/Wepn/PycharmProjects/wepn/python study/test.mp3', 'wb')

test_mp3_file.write(test_mp3)

test_mp3_file.close()
