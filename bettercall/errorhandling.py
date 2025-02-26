import logging
from flask import Flask, render_template

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def index():
    app.logger.info('Index page accessed')
    return 'Welcome to the Fundraising App!'

@app.route('/cause_error')
def cause_error():
    try:
        # This will cause a ZeroDivisionError
        result = 1 / 0
    except ZeroDivisionError as e:
        app.logger.error(f'An error occurred: {e}')
        return 'An error occurred. Check the logs for details.'

@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning('404 error occurred')
    return 'This page does not exist', 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error('500 error occurred')
    return 'An internal server error occurred', 500

if __name__ == '__main__':
    app.run(debug=True)
