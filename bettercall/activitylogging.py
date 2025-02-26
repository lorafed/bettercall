from flask import Flask, request, g
import logging

app = Flask(__name__)

# Setup activity logging
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.before_request
def log_user_activity():
    user = g.get('user', 'anonymous')
    activity = f"User: {user}, Path: {request.path}, Method: {request.method}, IP: {request.remote_addr}"
    logging.info(activity)

@app.route('/')
def index():
    return "Welcome to the fundraising app!"

@app.route('/donate', methods=['POST'])
def donate():
    return "Donation processed!"

if __name__ == '__main__':
    app.run(debug=True)
