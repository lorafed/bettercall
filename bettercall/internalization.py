from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Return the user's preferred language
    return request.accept_languages.best_match(['en', 'es', 'fr'])

@app.route('/')
def index():
    return render_template('index.html', title=_('Welcome'))

if __name__ == '__main__':
    app.run(debug=True)
