from flask import Flask, jsonify
from flask_caching import Cache

app = Flask(__name__)

# Configure Flask-Caching
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

@app.route('/data')
@cache.cached(timeout=60)
def get_data():
    # Simulate a slow query
    import time
    time.sleep(5)
    return jsonify({'data': 'This is some cached data'})

if __name__ == '__main__':
    app.run(debug=True)
