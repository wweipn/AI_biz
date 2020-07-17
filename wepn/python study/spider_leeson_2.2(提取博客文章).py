import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
soup = BeautifulSoup(res.text, 'html.parser')

name = soup.find_all('h2', class_='entry-title')
article = soup.find_all('div', class_='entry-summary')
published_time = soup.find_all('time', class_='entry-date published')

a = 0
for i in range(len(name)):
    print(published_time[a].text)
    print(name[a].text.strip())
    print(article[a].text.strip(), '\n')
    a = a + 1
