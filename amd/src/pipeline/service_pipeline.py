# -*- coding: utf-8 -*-
"""
Created on 2023-11-16

@author: Md Mamunur Rahman, PH: +1 6474473215
"""

from src.pipeline.action_manager import ActionResult

action_result = ActionResult()

#Final response for user
def gpt_response_for_user(request):
    
    response = {"response_id": generate_uuid(), "response": action_result.final_action_result(request) }
    return response

def generate_uuid():
    import uuid
    uuid = uuid.uuid4()
    return uuid


