from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    searchword = request.form.get('searchword')
    return render_template('main.html', searchword=searchword)

