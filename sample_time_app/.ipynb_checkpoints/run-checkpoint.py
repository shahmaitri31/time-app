from flask import Flask
from datetime import datetime,timedelta
import time 

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def timeofday():
    present = datetime.now() - timedelta(hours = 4, minutes = 0)
    return present.strftime('%H:%M:%S')

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
