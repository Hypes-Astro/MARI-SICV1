from flask import Flask, request

app = Flask(__name__)

# Rute untuk menerima data melalui metode GET
@app.route('/get_data', methods=['GET'])
def get_data():
    data = request.args.get('data')
    # Lakukan pemrosesan data sesuai kebutuhan
    print(f'Data received via GET: {data}')
    return 'Data received successfully'

# Rute untuk menerima data melalui metode POST
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.form.get('data')
    # Lakukan pemrosesan data sesuai kebutuhan
    print(f'Data received via POST: {data}')
    return ('Data post')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# RUN : 
# 1. env\Scripts\activate
# 2. python app.py