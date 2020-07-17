import requests
from bs4 import BeautifulSoup


res = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(res.text, 'html.parser')

"""
第一个练习
"""
books = soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li')
for book in books:
    print(book.text.strip())


"""
第二个练习
"""
book_list = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for book in book_list:
    book_name = book.find('h3').find('a')
    book_price = book.find('p', class_='price_color')
    book_star = book.find('p')
    print('书名:', book_name['title'])
    print('价格:', book_price.text[2:])
    if book_star['class'][-1] == 'One':
        print('评价: 一星\n')
    if book_star['class'][-1] == 'Two':
        print('评价: 二星\n')
    if book_star['class'][-1] == 'Three':
        print('评价: 三星\n')
    if book_star['class'][-1] == 'Four':
        print('评价: 四星\n')
    if book_star['class'][-1] == 'Five':
        print('评价: 五星\n')