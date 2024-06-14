from flask import Flask, request

app = Flask(__name__)

# Rute untuk menerima data melalui metode GET
Data = []
@app.route('/get_data', methods=['GET'])
def get_data():
    print(f'Data received via GET: ')
    return Data

# Rute untuk menerima data melalui metode POST
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.form.get('data')
    print(f'Data received via POST: {data}')
    Data.append(data)
    return ('Data post')
    
# Rute untuk menerima data melalui metode PUT

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# RUN : 
# 1. env\Scripts\activate
# 2. python app.py