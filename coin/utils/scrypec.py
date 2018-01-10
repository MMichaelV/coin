import requests
import pickle
from bs4 import BeautifulSoup as bs
import csv
from django.utils import timezone
from django import db
from ..models import Coin

def scrype_new_coins():
    print('This working method scrype')
    # url_base = 'https://coinmarketcap.com'
    # url_start = 'https://coinmarketcap.com/all/views/all/'
    # headers = {
    #     # "Authorization": "Michael" + accessToken,
    #     # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     # 'Cashe-Control': 'max-age=0',
    #     # 'Connection': 'keep-alive',
    #     # 'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    # }
    # fl_debug = True
    # if fl_debug:
    #     with open('./coins/razn_data/pgsaved.pkl', 'rb') as f:
    #         rescontent = pickle.load(f)
    # else:
    #     r = requests.get(url_start, headers=headers)
    #     # print(r.status_code)
    #     rescontent = r.content
    #     with open('./coins/razn_data/pgsaved.pkl', 'wb') as f:
    #         pickle.dump(rescontent, f)
    # soup = bs(rescontent, 'lxml')
    # res = soup.find('table', class_='js-summary-table').find('tbody').find_all('tr')
    # with open('./coins/razn_data/newcoins.csv', 'w', newline='') as f:
    #     fieldnames = ['coin', 'name', 'datePrice', 'currentPrice', 'link_to_exch', 'fl_added']
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     writer.writeheader()
    #     dstamp = timezone.now()
    #     for obj in res:
    #         coins = {}
    #         coins['coin'] = obj.find('td', class_='col-symbol').string
    #         coins['name'] = obj.find('a', class_='currency-name-container').string
    #         coins['datePrice'] = dstamp
    #         coins['currentPrice'] = obj.find('a', class_='price')['data-usd']
    #         coins['link_to_exch'] = url_base + obj.find('a', class_='currency-name-container')['href']
    #         coins['fl_added'] = 'True'
    #         writer.writerow(coins)
    # print('Write complete')

def import_new_coins():
    print('This working method import scryped')
    # count = Coins.objects.all().update(fl_added='False')
    # print('Clear', count, 'record with flag added before update')
    # with open('./coins/razn_data/newcoins.csv', 'r', newline='') as f:
    #     reader = list(csv.DictReader(f))
    # for row in reader:
    #     c = Coins(**row)
    #     try:
    #         c.save(force_insert=True)
    #     except db.IntegrityError:
    #         print(row['name'], 'exist, not save')
