from flask import Flask
from Customer_Personality.logger.logs import logging
from Customer_Personality.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    try:
        raise Exception('custom exception')
    except Exception as e:
        custom= CustomException(e, sys)
        return 'hello world'
    

if __name__ == '__main__':
    app.run(debug=True)