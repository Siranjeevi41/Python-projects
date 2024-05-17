from flask import Blueprint, request, jsonify
from services.chatgpt_service.py import get_chatgpt_response
from services.bridgeit_service.py import get_bridgeit_response
from utils.logger import setup_logger

api_controller = Blueprint('api_controller', __name__)
logger = setup_logger(__name__)

@api_controller.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.get_json()
    query = data.get('query')
    service = data.get('service')

    try:
        if service == 'chatgpt':
            response = get_chatgpt_response(query)
        elif service == 'bridgeit':
            response = get_bridgeit_response(query)
        else:
            return jsonify({'message': 'Invalid service'}), 400

        return jsonify({'response': response}), 200
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        return jsonify({'message': 'Error processing query'}), 500
