from bs4 import BeautifulSoup as bs
import requests, cloudscraper, json

def wattpad(text):
    req = cloudscraper.create_scraper()
    url = 'https://www.wattpad.com/search/'+text
    has = bs(req.get(url).content,
             'html.parser').find('div', class_='story-card-data hidden-xxs')
    base = bs(req.get(url).content,
              'html.parser')
    mak = base.find('div', class_='title').text.strip()
    mok = base.find('div', class_='description').text.strip()
    img = base.find('div', class_='cover').find('img')['src']
    stat = base.find('div', class_='tag-item').text.strip()
    return {
        'title':mak,
        'desk':mok,
        'gambar':img,
        'status':stat
    }