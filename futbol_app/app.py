from flask import Flask



app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

@app.route('/')
def index():
    return 'Canchas Viejo Carlos'