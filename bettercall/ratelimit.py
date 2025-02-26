from flask import Flask, jsonify
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/data')
@limiter.limit("5 per minute")
def get_data():
    return jsonify({"message": "This is protected data"})

if __name__ == '__main__':
    app.run(debug=True)
