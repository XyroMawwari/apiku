from bs4 import BeautifulSoup as bs
import requests, cloudscraper, json

def fastdlapp(link):
    req = cloudscraper.create_scraper()
    process = bs(req.post('https://fastdl.app/c/', data={'url':link, 'lang_code':'id', 'token':''}).text, 'html.parser')
    image = process.find('img')['src']
    download = process.find('a', id='download-btn')['href']
    return {
        'image':image,
        'download':download
    }