#!/usr/bin/python

import urllib
import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup


def get_content(url, data=None):
    print(url)
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            ''' 
            rep = requests.get(url,headers = header,timeout = timeout)
            rep.encoding = 'utf-8'
            req = urllib.request.Request(url, data, header)
            response = urllib.request.urlopen(req, timeout=timeout)
            html_text = response.read().decode('UTF-8', errors='ignore')
            response.close()
            '''
            break
        # except urllib.request.HTTPError as e:
        #         print( '1:', e)
        #         time.sleep(random.choice(range(5, 10)))
        #
        # except urllib.request.URLError as e:
        #     print( '2:', e)
        #     time.sleep(random.choice(range(5, 10)))
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))

    # return rep.text
    # return html_text


def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    data = body.find('div', {'id': '7d'})
    ul = data.find('ul')
    li = ul.find_all('li')

    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)
        inf = day.find_all('p')
        temp.append(inf[0].string, )
        if inf[1].find('span') is None:
            temperature_highest = None
        else:
            temperature_highest = inf[1].find('span').string
            temperature_highest = temperature_highest.replace('℃', '')
        temperature_lowest = inf[1].find('i').string
        temperature_lowest = temperature_lowest.replace('℃', '')
        temp.append(temperature_highest)
        temp.append(temperature_lowest)
        final.append(temp)

    return final


def write_data(data, name):
    file_name = name
    ''' 
    with open(file_name, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)
    '''


if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101190401.shtml'
    html = get_content(url)
    result = get_data(html)
    write_data(result, 'weather.csv')
