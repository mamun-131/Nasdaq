# Ask Market Data


## Table of Contents
- [Ask Market Data](#Ask Market Data)
    - [Table of Contents](#table-of-contents)
    - [Overview](#overview)
    - [Development](#development)
    - [Install Dependencies](#install-dependencies)
    -[Outcomes](#outcomes)


## Overview
This app has been developed to showcase Python API calls, Openai Chatgpt Prompt engineering, and NLP based API query. I have taken a dummy csv data file for a data query. If you use this code you have to apply your own access key in .env.example file as json format like
{"OPENAI_API_KEY" : "sk-cQxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}  


## Development
There is a main app.py file to run the app. Other files are decentralized and kept in different folders src main folder. For data and logs there are separate folders.
- api folder has api.py file for api coding.
- components folder has openai_gpt_prompt.py file which manage to call openai API
- pipeline folder has 2 files; action_manager.py which manage all the actions like entity extraction, data query and response. service_pipeline.py shape up final response with response id.




## Install Dependencies
The following packages are needed to be installed. But I have created a setup.py file which will install all the dependency. You need to run the command "python setup.py install". Apart from this there is a docker file to create docker containers.


- openai
- json
- panda
- numpy
- openai
- uuid
- flask==2.1.3


## Outcomes
API Endpoint : https://localhost:5000/api/v1/marketdataquery
JSON Body : {"query": "What is the volume for tesla today?"}


You can ask questions like..
{"query": "What is the volume for tesla today?"}


You will get the response. :)
{
    "response": "The volume for Tesla today is 0.11 million shares.",
    "response_id": "0f7aff55-4133-4751-8351-d12d9ab933af"
}

