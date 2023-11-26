# -*- coding: utf-8 -*-
"""
Created on 2023-11-16

@author: Md Mamunur Rahman, PH: +1 6474473215
"""
import json
import os
import sys
from src.exception import CustomException
from src.logger import logging


def get_openai_key():
    filepath = os.getcwd() + "/src/"
    apikey=""
    with open(r"" + filepath + ".env.example", "r") as readfile:
        apikey = json.load(readfile)["OPENAI_API_KEY"]
        logging.info(apikey)
    return apikey 


