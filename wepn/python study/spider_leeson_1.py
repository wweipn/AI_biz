import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

a = open('D:/Users/Wepn/PycharmProjects/wepn/html_code.txt', 'a+', encoding='utf-8')
a.write(res.text)
a.close()

