# -*- coding: utf-8 -*-
"""
Created on 2023-11-16

@author: Md Mamunur Rahman, PH: +1 6474473215
"""
import os
import sys
 
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import json
from components.openai_gpt_prompt import OpenAIGptPrompt
import utils as common
import pandas as pd
import json
from src.logger import logging

BASE_PATH = str(os.getcwd())

df = pd.read_csv(BASE_PATH + "/data/EndOfDayData_2023-05-30.csv")

# GPT call for intent classification and entity extraction
def intent_classification(user_query):
    chatgpt = OpenAIGptPrompt()
    instruction = "You are an intent classifier and entiry extractor. You have to analyze stock exchange share sales and price data of different companies. "
    instruction = instruction + "There are only 6 intents; volume, low, high, open, close, last. For your information low, high, open, close and last are prices of shares like low price, high price etc. "
    instruction = instruction + "If users query does not fall into these 6 cagegories then response with fallback intent. "
    instruction = instruction + "Also extract symbol or company code from user query. Response must be in JSON format. "
    instruction = instruction + 'Response example: [{"intent":"volume", "symbol":"AAPL"}]'
    chat_prompt_responses = chatgpt.chatgpt_prompt(user_query, instruction)
    return chat_prompt_responses 

#Data Table query
def data_extraction(intent_entity):
    symbol = json.loads(intent_entity)[0]['symbol']
    intent = json.loads(intent_entity)[0]['intent']
    data = df.loc[df['symbol'] == symbol]	
    json_data = data.to_json(orient='records')
    return [{"market_info":json_data, "intent":intent}]

#GPT callfor finalresponse
def final_user_response(user_query, data_query_result):
    chatgpt = OpenAIGptPrompt()
    instruction = "You are an inteliget vertual assistant. Based on user query on share market information we have retrive JSON data market_info from database and also the intent"
    instruction = instruction + "Your responsibility is to cretae appropriate response based on JSON date and user query. You must mention the symbol or company code in your response. Example: Apple(AAPL)"
    instruction = instruction + "Just take a note that volumes of sales are in millions shares and price are in usd. "
    instruction = instruction + "JSON Data: " + str(data_query_result)
    chat_prompt_responses = chatgpt.chatgpt_prompt(user_query, instruction)
    return chat_prompt_responses 

#Final action response
class ActionResult:
    def __init__(self):
        self
    def final_action_result(self,user_query):
        return final_user_response(user_query, data_extraction(intent_classification(user_query)))
    
