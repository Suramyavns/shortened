from flask import Flask,redirect,jsonify,request
from crud import *

app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    return jsonify({'message':'This is URL shortener'})

@app.route('/get_url',methods=['POST'])
def fetch_url():
    try:
        uuid = request.get_json()['uuid']
    except:
        return jsonify({'message':'Provide correct uuid!'})
    else:
        url = get_url(uuid)
        if url:
            return jsonify({'url':url})
        return jsonify({'message':'Invalid uuid!'})

@app.route('/add_url',methods=['POST'])
def insert_url():
    data = request.get_json()
    try:
        uuid = add_url(str(data['url']))
        if uuid:
            return jsonify({'uuid':uuid})
        return jsonify({"messsage":'Invalid url!'})
    except:
        return jsonify({'message':'URL not specified'})

@app.route('/<string:uuid>')
def go_to(uuid):
    url = get_url(uuid)
    if url:
        return redirect(url)
    return jsonify('BAD REQUEST')

if __name__=='__main__':
    app.run(debug=True)