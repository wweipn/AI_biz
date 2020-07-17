from bs4 import BeautifulSoup
import requests
import time

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.106 Safari/537.36'}
res = requests.get('http://www.xiachufang.com/explore/', headers=header)
soup = BeautifulSoup(res.text, 'html.parser')
recipe = soup.find_all('div', class_='info pure-u')
recipe_list = []
a = 0
for i in recipe:
    print(i.find('p').find('a').text.strip())
    recipe_list.append({i.find('p').find('a').text.strip(): []})
    shicai = i.find('p', class_='ing ellipsis').find_all('a', target='_blank')
    print('食材:')
    for n in shicai:
        print(n.text)
        recipe_list[a][i.find('p').find('a').text.strip()].append(n.text)
    a = a + 1
    print('\n')
    time.sleep(1)

print(recipe_list)

