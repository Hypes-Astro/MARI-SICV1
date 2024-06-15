import pymongo # meng-import library pymongo yang sudah kita install
from flask import Flask
from flask import request
app = Flask(__name__)

password = 'sic123'
uri= f"mongodb+srv://alifSic:{password}@sic.ajunnqj.mongodb.net/?retryWrites=true&w=majority&appName=sic"

client = pymongo.MongoClient(uri)
db = client['challenge1'] # ganti sesuai dengan nama database kalian
my_collections = db['sensor'] # ganti sesuai dengan nama collections kalian

def ambil_data_kelembapan():
    list_kelembapan = []
    for x in my_collections.find():
      list_kelembapan.append(x['kelembapan'])
    
    hasil = sum(list_kelembapan)/len(list_kelembapan)
    return str(hasil)

def ambil_data_temperature():
    list_temperature = []
    for x in my_collections.find():
      list_temperature.append(x['temperature'])
    
    hasil = sum(list_temperature)/len(list_temperature)
    return str(hasil)

def ambil_data_kelembapan_all():
    list_kelembapan = []
    for x in my_collections.find():
      list_kelembapan.append(x['kelembapan'])
    
    return list_kelembapan

def ambil_data_temperature_all():
    list_temperature = []
    for x in my_collections.find():
      list_temperature.append(x['temperature'])
    
    return list_temperature

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/sensor1/temperature/avg',methods=[ 'GET'])
def temperature():
    return ambil_data_temperature()

@app.route('/sensor1/kelembapan/avg',methods=[ 'GET'])
def kelembapan():
    return ambil_data_kelembapan()

@app.route('/sensor1/temperature/all',methods=[ 'GET'])
def temperature_all():
    return ambil_data_temperature_all()

@app.route('/sensor1/kelembapan/all',methods=[ 'GET'])
def kelembapan_all():
    return ambil_data_kelembapan_all()

if __name__ == '__main__':
   app.run(host='0.0.0.0')