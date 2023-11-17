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

BASE_PATH = str(os.getcwd())

df = pd.read_csv(BASE_PATH + "\data\sales_csv\sales.csv")

# GPT call for intent classification and entity extraction
def intent_classification(user_query):
    chatgpt = OpenAIGptPrompt()
    instruction = "You are an intent classifier and entiry extractor. There are only 2 intents; price and volume. "
    instruction = instruction + "If users query does not fall into these 2 cagegory then response with fallback intent. "
    instruction = instruction + "Also extract company code from user query. Response must be in JSON format."
    instruction = instruction + 'Response example: [{"intent":"price", "company_code":"AAPL"}]'
    chat_prompt_responses = chatgpt.chatgpt_prompt(user_query, instruction)
    return chat_prompt_responses 

#Data Table query
def data_extraction(intent_entity):
    company_code = json.loads(intent_entity)[0]['company_code']
    intent = json.loads(intent_entity)[0]['intent']
    data = df.loc[df['Symbol'] == company_code]	
    json_data = data.to_json(orient='records')
    """if intent == 'price':
        result = json.loads(json_data)[0]['Price']
    if intent == 'quantity':
        result = json.loads(json_data)[0]['Volume']"""
    return json_data

#GPT callfor finalresponse
def final_user_response(user_query, data_query_result):
    chatgpt = OpenAIGptPrompt()
    instruction = "You are an inteliget vertual assistant. Based on user query on share market information we have retrive JSON data from database "
    instruction = instruction + "Your responsibility is to cretae appropriate response based on JSON date and user query. "
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
    
