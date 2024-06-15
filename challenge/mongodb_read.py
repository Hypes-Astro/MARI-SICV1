import pymongo # meng-import library pymongo yang sudah kita install

password = 'sic123'
uri= f"mongodb+srv://alifSic:{password}@sic.ajunnqj.mongodb.net/?retryWrites=true&w=majority&appName=sic"

client = pymongo.MongoClient(uri)
db = client['test_database'] # ganti sesuai dengan nama database kalian
my_collections = db['test_collection'] # ganti sesuai dengan nama collections kalian

for x in my_collections.find():
 print(x)