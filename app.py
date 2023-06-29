from flask import Flask, render_template, request, jsonify, make_response, send_file
import requests
import qrcode
from data.online import online
from data.fandomgt import gtfandom
from data.pricegt import price
from data.sertitolol import serti
from data.wattpad import wattpad
from data.artinama import arti
from data.bmkg import bmkg
from data.rainy import rainy
from data.igdl import fastdlapp
import os, json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def api():
    return render_template('api_s.html')

@app.route('/api/onlinegt', methods=['GET', 'POST'])
def onlinegt():
    on = online()
    print(on)
    return {"online":on}

@app.route('/api/gtwiki', methods=['GET', 'POST'])
def gtwiki():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return gtfandom(keyword)
    else:
        return {'error':"Keyword Input Please"}

@app.route('/api/gtprice', methods=['GET', 'POST'])
def pricegt():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return price(keyword)
    else:
        return {'error':"Keyword Input Please"}
    
@app.route('/api/sertitolol', methods=['GET', 'POST'])
def sertis():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return serti(keyword)
    else:
        return {'error':"Keyword Input Please"}
    
@app.route('/api/wattpad', methods=['GET', 'POST'])
def wattpads():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return wattpad(keyword)
    else:
        return {'error':"Keyword Input Please"}
    
@app.route('/api/artinama', methods=['GET', 'POST'])
def artinamas():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return arti(keyword)
    else:
        return {'error':"Keyword Input Please"}
    
@app.route('/api/qrgen', methods=['GET','POST'])
def qrcode_gen():
    if request.args.get('keyword'):
        try:
            input_data = request.args.get('keyword')
            qr = qrcode.QRCode(
            version=2,
            box_size=15,
            border=2)
            qr.add_data(input_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save('data/qrcode.png')
            return send_file('data/qrcode.png')
        except Exception as e:
            print(e)
            return{
                'result': 'Gagal membuat qr!'
            }
    else:
        return{
            'result': 'Masukkan parameter text!'
        }
        
@app.route('/api/rainy', methods=['GET', 'POST'])
def rainys():
    if (request.args.get('keyword')):
        keyword = request.args.get("keyword")
        return rainy(keyword)
    else:
        return {'error':"Keyword Input Please"}
    
@app.route('/api/bmkg', methods=['GET', 'POST'])
def bmkgs():
    mama = bmkg()
    return mama

@app.route('/api/igdl', methods=['GET', 'POST'])
def igdl():
    if (request.args.get('url')):
        url = request.args.get("url")
        return fastdlapp(url)
    else:
        return {'error':"Url Input Please"}

app.run(host='0.0.0.0', port=int(os.environ.get('port','5000')),debug=True)