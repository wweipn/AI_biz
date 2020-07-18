from bs4 import BeautifulSoup
import requests
import time

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/83.0.4103.106 Safari/537.36'}
res = requests.get('http://www.xiachufang.com/explore/', headers=header)
soup = BeautifulSoup(res.text, 'html.parser')
recipe = soup.find_all('div', class_='info pure-u')
"""
方法一
"""
# recipe_list = []
# a = 0
# for i in recipe:
#     print(i.find('p').find('a').text.strip())
#     recipe_list.append({i.find('p').find('a').text.strip(): []})
#     shicai = i.find('p', class_='ing ellipsis').find_all('a', target='_blank')
#     print('食材:')
#     for n in shicai:
#         print(n.text)
#         recipe_list[a][i.find('p').find('a').text.strip()].append(n.text)
#     a = a + 1
#     print('\n')
#     time.sleep(1)
#
# print(recipe_list)

"""
方法二
"""
# 获取第一个菜名
# tag_a = recipe[0].find('a')
# print(tag_a.text.strip())
#
# # 获取第一个菜名的食材
# tag_p = recipe[0].find('p', class_='ing ellipsis')
# print(tag_p.text.strip())
# recipe_list = []
# for i in recipe:
#     print(i.find('a').text.strip())
#     print(i.find('p', class_='ing ellipsis').text.strip(), '\n')
#     recipe_list.append(['菜名:{},链接:http://www.xiachufang.com/{},食材:{}'.format(i.find('a').text.strip(),
#                                              i.find('a')['href'], i.find('p', class_='ing ellipsis').text.strip())])
# print(recipe_list)

"""
方法三
"""
recipe_list = []
for i in range(len(recipe)):
    recipe_name = recipe[i].find('p', class_='name').text.strip()
    recipe_url = 'http://www.xiachufang.com/{}'.format(recipe[i].find('p', class_='name').find('a')['href'])
    recipe_details = recipe[i].find('p', class_='ing ellipsis').text.strip()
    recipe_list.append([recipe_name, recipe_url, recipe_details])
print(recipe_list)
