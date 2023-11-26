
import os
import sys
from src.logger import logging
from flask import Flask
from src.api.api import api_blueprint


app = Flask(__name__)

#API Call
app.register_blueprint(api_blueprint)
logging.info("App has been started.")

"""
#Run app
if __name__ == '__main__':
   app.run(debug = True, ssl_context='adhoc', port=5000)
   #app.run()
   
"""
