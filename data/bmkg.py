from bs4 import BeautifulSoup as bs
import requests, cloudscraper, json

def bmkg():
    home = bs(requests.get('https://www.bmkg.go.id/').content,
              'html.parser').find('div', class_='gempabumi-home-bg margin-top-13')
    gambar = home.find('img')['src']
    li = home.find('ul').findAll('li')
    waktu = li[0].text
    magnitudo = li[1].text
    kedalaman = li[2].text
    koordinat = li[3].text
    lokasi = li[4].text
    dirasakan = li[5].text
    return {
        'gambar':gambar,
        'waktu':waktu,
        'magnitudo':magnitudo,
        'kedalaman':kedalaman,
        'koordinat':koordinat,
        'lokasi':lokasi,
        'dirasakan':dirasakan
    }