from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-tokens')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':  # Simplified password check
        token = jwt.encode({'username': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Could not verify login!'}), 401

@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return f'Hello {current_user}, you have accessed a protected route!'

if __name__ == '__main__':
    app.run(debug=True)
