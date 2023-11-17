
import os
import sys
from src.exception import CustomException
from src.logger import logging
from flask import Flask, render_template, request
from src.api.api import api_blueprint


app = Flask(__name__,template_folder='template')

#API Call
app.register_blueprint(api_blueprint)

#Run app
if __name__ == '__main__':
   app.run(debug = True, ssl_context='adhoc')

