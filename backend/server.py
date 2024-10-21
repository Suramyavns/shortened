'''
This is the main module for this server backend
'''
from flask import Flask,render_template,redirect,jsonify,request
from crud import add_url,get_url

app = Flask(__name__)

@app.route('/')
def root():
    '''
    This will return a simple html page showing no content here
    '''
    return render_template('no-content.html')

@app.route('/get_url')
def fetch_url():
    '''
    This is fetch the URL from given id in request data if method is POST.
    Returns bad-request page for GET request on this API
    '''
    method = request.method
    if method=='POST':
        try:
            uuid = request.get_json()['uuid']
        except:
            return jsonify({'message':'Provide correct uuid!'})
        url = get_url(uuid)
        if url:
            return jsonify({'url':url})
        return jsonify({'message':'Invalid uuid!'})
    return render_template('bad-request.html')
@app.route('/add_url')
def insert_url():
    '''
    This is add the given URL in request body if method is POST.
    Returns bad-request page for GET request on this API
    '''
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
    '''
    This function will redirect the user to the correct URL
    '''
    url = get_url(uuid)
    if url:
        return redirect(url)
    return render_template('not-found.html')

if __name__=='__main__':
    app.run(debug=True)
