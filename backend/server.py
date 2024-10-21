from flask import Flask,render_template,redirect,jsonify,request
from crud import *

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('no-content.html')

@app.route('/get_url')
def fetch_url():
    method = request.method
    if method=='POST':
        try:
            uuid = request.get_json()['uuid']
        except:
            return jsonify({'message':'Provide correct uuid!'})
        else:
            url = get_url(uuid)
            if url:
                return jsonify({'url':url})
            return jsonify({'message':'Invalid uuid!'})
    return render_template('bad-request.html')
@app.route('/add_url')
def insert_url():
    method = request.method
    if method=='POST':
        data = request.get_json()
        try:
            uuid = add_url(str(data['url']))
            if uuid:
                return jsonify({'uuid':uuid})
            return jsonify({"messsage":'Invalid url!'})
        except:
            return jsonify({'message':'URL not specified'})
    return render_template('bad-request.html')
@app.route('/<string:uuid>')
def go_to(uuid):
    url = get_url(uuid)
    if url:
        return redirect(url)
    return render_template('not-found.html')

if __name__=='__main__':
    app.run(debug=True)