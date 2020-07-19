import requests

payload = {'ct': '24',
           'qqmusic_ver': '1298',
           'new_json': '1',
           'remoteplace': 'txt.yqq.song',
           'searchid': '56260068745991392',
           't': '0',
           'aggr': '1',
           'cr': '1',
           'catZhida': '1',
           'lossless': '0',
           'flag_qc': '0',
           'p': '1',
           'n': '10',
           'w': '周杰伦',
           'g_tk_new_20200303': '5381',
           'g_tk': '5381',
           'loginUin': '0',
           'hostUin': '0',
           'format': 'json',
           'inCharset': 'utf8',
           'outCharset': 'utf-8',
           'notice': '0',
           'platform': 'yqq.json',
           'needNewCode': '0'}

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.106 Safari/537.36'}

res = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp', params=payload, headers=headers)
res_json = res.json()
song_list = res_json['data']['song']['list']
for i in range(len(song_list)):
    # print(type(song_list[i]['id']))
    payload1 = {'nobase64': '1',
                'musicid': str(song_list[i]['id']),
                '-': 'jsonp1',
                'g_tk_new_20200303': '5381',
                'g_tk': '5381',
                'loginUin': '0',
                'hostUin': '0',
                'format': 'json',
                'inCharset': 'utf8',
                'outCharset': 'utf-8',
                'notice': '0',
                'platform': 'yqq.json',
                'needNewCode': '0'}
    headers1 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
                'referer': 'https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html',
                'origin': 'https://y.qq.com',
                'accept': 'application/json, text/javascript, */*; q=0.01'}
    res1 = requests.get('https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg', headers=headers1, params=payload1)
    lyric = res1.json()['lyric']
    print(lyric)