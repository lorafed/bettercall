from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='api_requests.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.before_request
def log_request_info():
    logging.info(f'Request: {request.method} {request.url} - Body: {request.get_data()}')

@app.after_request
def log_response_info(response):
    logging.info(f'Response: {response.status} - Body: {response.get_data()}')
    return response

@app.route('/data', methods=['POST'])
def data():
    content = request.json
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)
