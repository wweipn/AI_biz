import requests
from bs4 import BeautifulSoup
import time

n = 0
a = 1
movies_list = []
while n < 250:
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    res = requests.get('https://movie.douban.com/top250?start={}&filter'.format(n), headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    movies = soup.find_all('div', class_='item')
    for i in range(len(movies)):
        try:
            number = movies[i].find('div', class_='pic').text.strip()
            title = movies[i].find('span', class_='title').text.strip()
            quote = movies[i].find('p', class_='quote').text.strip()
            rating_num = movies[i].find('span', class_='rating_num').text.strip()
            link = movies[i].find('a')['href']
            movies_list.append(['编号:{},电影名称:{},简介:{},评分:{},链接{}'.format(number, title, quote, rating_num, link)])
        except AttributeError:
            pass
    print('第{}页爬取完成,已爬取{}条数据'.format(a, len(movies_list)))
    n = n + 25
    a = a + 1
    time.sleep(1)
print('爬取完成,数据如下:\n{}'.format(movies_list))
