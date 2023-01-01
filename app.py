from flask import Flask
from ccDefault.logger import logging
from ccDefault.exception import CCDefaultException
import sys

app = Flask(__name__)

@app.route('/')
def index():
    try:
        raise Exception('We are testing Custom Exception')
    except Exception as e:
        ccDefault = CCDefaultException(e, sys)
        logging.info(ccDefault.error_message) 
        logging.info('We are testing logging module')
    return "Welcome"

if __name__ == '__main__':
    app.run(debug=True)