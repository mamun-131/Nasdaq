# Ask Market Data


## Table of Contents
- [Ask Market Data](#Ask Market Data)
    - [Table of Contents](#table-of-contents)
    - [Overview](#overview)
    - [Development](#development)
    - [Install Dependencies](#install-dependencies)
    -[Outcomes](#outcomes)


## Overview
This app has been developed to showcase Python API calls, Openai Chatgpt Prompt engineering, and NLP based API query. I have taken the csv data file for a data query. This apprequires OpenAI API Key. I have notincluded my api key for openai. So, apply your own access key in .env.example file as json format like
{"OPENAI_API_KEY" : "sk-cQxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}  


## Development
There is a main app.py file to run the app. Other files are decentralized and kept in different folders src main folder. For data and logs there are separate folders.
- api folder has api.py file for api coding.
- components folder has openai_gpt_prompt.py file which manages to call openai API
- pipeline folder has 2 files; action_manager.py which manage all the actions like entity extraction, data query and response. service_pipeline.py shape up final response with response id.




## Install Dependencies
The following packages are needed to be installed. But you need to run the docker commands which i have written in my_docker_command.txt file. However, I have given the full list of docker command and guide in below.
- openai
- json
- pandas
- numpy
- uuid
- flask==2.1.3
- Werkzeug==2.0.2
- cryptography

Go to app path first: ~/AMD
After that apply docker command in CMD. Make sure you have desktop docker installed and its running.
Docker commands:
- build docker
command: docker build -t amd-app .
- run docker
command: docker run -d -p 5000:5000 amd-app

- Once you run the docker image, you can now call the api. I have kept http (not htpps) just to avoid ssl issue in localhost during demonstration. 
http://localhost:5000/api/v1/marketdataquery

- see running docker
command: docker ps
- stop docker image
command: docker stop "container ID"
- see number of docker image
command: docker images
- docker image remove
command: docker image rm -f amd-app


## Outcomes
API Endpoint : http://localhost:5000/api/v1/marketdataquery
JSON Body : {"query": "What is the volume for tesla today?"}


You can ask questions like..
{"query": "What is the volume for tesla today?"}


You will get the response. :)
{
    "response": "The volume for Tesla (TSLA) today is 0.11 million shares.",
    "response_id": "0f7aff55-4133-4751-8351-d12d9ab933af"
}

You can ask questions like..
{"query": "What is the last price of microsoft today?"}
You will get the response. :)
{
    "response": "The last price of Microsoft (MSFT) today is $331.21.",
    "response_id": "4eecdf3e-e880-4870-9cdb-b353e3f51ca6"
}
