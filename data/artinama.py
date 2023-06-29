from bs4 import BeautifulSoup as bs
import requests, cloudscraper,json

def arti(text):
    url = 'https://primbon.com/arti_nama.php?nama1='+text
    html = '&proses=+Submit%21+'
    hi = url+html
    ra = bs(requests.get(hi).text,
            'html.parser').find('div', id='body').text.strip().split('\n')
    artik = ra[8]
    return {
        'arti':artik
    }
    
    