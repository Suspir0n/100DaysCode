from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    result = 2 + 2
    return 'Soma: {}'.format(result)
    