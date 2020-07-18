import requests  # 调用requests库
from bs4 import BeautifulSoup  # 调用BeautifulSoup库

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all(class_='comment-content')
for item in items:
    comment = item.find('p')
    print(comment.text)


