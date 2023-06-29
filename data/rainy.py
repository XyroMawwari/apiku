from bs4 import BeautifulSoup as bs
import requests, cloudscraper, json

def rainy(text):
     r = cloudscraper.create_scraper()
     url = 'https://ephoto360.com/hieu-ung-viet-chu-len-cua-kinh-mua-tam-trang-dep-682.html'
     be = bs(r.get(url).text, 'html.parser')
     token = be.find('input', attrs={'name': 'token'})['value']
     #radio = random.choice(['05acf523-6deb-4b9d-bb28-abc4354d0858', '843a4fc2-059c-4283-87e4-c851c013073b', 'd951e4be-450e-4658-9e73-0f7c82c63ee3', 'a5b374f3-2f29-4da4-ae15-32dec01198e2'])
     build_server = be.find('input', attrs={'name': 'build_server'})['value']
     build_server_id = be.find('input', attrs={'name': 'build_server_id'})['value']
     data = {'text[]': text, 'submit': 'Create a photo', 'token': token, 'build_server': build_server, 'build_server_id': build_server_id}
     bes = bs(r.post(url, data).text, 'html.parser')
     fv = bes.find('input', id='form_value_input')['value']
     js = json.loads(fv)
     res = r.post('https://ephoto360.com/effect/create-image', data={'id': '702', 'text[]': text, 'token': js['token'], 'build_server': build_server, 'build_server_id': build_server_id}).json()
     result = build_server+res['image']
     return {
         'result':result
     }