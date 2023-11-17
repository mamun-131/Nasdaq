from flask import Flask, Blueprint, jsonify, request
import src.pipeline.service_pipeline as SP

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

#API for market query
@api_blueprint.route('/marketdataquery', methods = ['POST'])
def market_data_query():
    query = request.json['query']
    gpt_response = SP.gpt_response_for_user(query)
    return jsonify(gpt_response)


