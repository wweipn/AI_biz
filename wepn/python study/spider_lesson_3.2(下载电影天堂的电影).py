import requests
from bs4 import BeautifulSoup
from urllib import parse
import time

# movie = input('请输入要下载的电影名称:')
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
res = requests.get('http://s.ygdy8.com/plus/s0.php?typeid=1&keyword={}'.format(parse.quote('无名之辈'.encode('gbk'))),
                   headers=header)
res.encoding = 'gbk'
soup = BeautifulSoup(res.text, 'html.parser')
search_result = soup.find_all('div', class_='co_content8')

# 获取到下载电影的链接
movie_detail_link = 'https://www.ygdy8.com{}'.format(search_result[0].find('a')['href'])
res1 = requests.get(movie_detail_link)
res1.encoding = 'gbk'
soup1 = BeautifulSoup(res.text, 'html.parser')
for i in range(len(search_result)):
    download_link = soup1.find('td', style='WORD-WRAP: break-word').text.strip()
    movie_name = soup.find('span', style='FONT-SIZE: 12px')[0].find('br').text
    download_movie = requests.get('download_link')
    movie_file = open('D:/Users/Wepn/PycharmProjects/wepn/{}'.format(movie_name.split('/')[-1]), 'wb')
    movie_file.write(download_movie.content)
    movie_file.close()
print(res1.status_code)
print(type(movie_detail_link))



# quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开

# movie = input('你想看什么电影呀？')
# gbkmovie = movie.encode('gbk')
# # 将汉字，用gbk格式编码，赋值给gbkmovie
# url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=' + parse.quote(gbkmovie)
# # 将gbk格式的内容，转为url，然后和前半部分的网址拼接起来。
# res = requests.get(url)
# # 下载××电影的搜索页面
# res.encoding = 'gbk'
# # 定义res的编码类型为gbk
# soup_movie = BeautifulSoup(res.text, 'html.parser')
# # 检测没有找到电影（无对应标签）时出现的异常信息
# try:
#     # 解析网页
#     urlpart = soup_movie.find(class_="co_content8").find_all('table')
#     # print(urlpart)
#     if urlpart:
#         urlpart = urlpart[0].find('a')['href']
#         urlmovie = 'https://www.ygdy8.com/' + urlpart
#         res1 = requests.get(urlmovie)
#         res1.encoding = 'gbk'
#         soup_movie1 = BeautifulSoup(res1.text, 'html.parser')
#         urldownload = soup_movie1.find('div', id="Zoom").find('span').find('table').find('a')['href']
#         print(urldownload)
#     else:
#         print('没有' + movie)
#         # 有些电影是查询不到没下载链接的，因此加了个判断
# # 捕获异常错误并执行下方子句
# except:
#     print('没有找到电影')