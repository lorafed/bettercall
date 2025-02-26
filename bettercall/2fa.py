import pyotp
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/generate_otp', methods=['GET'])
def generate_otp():
    totp = pyotp.TOTP('base32secret3232')
    otp = totp.now()
    session['otp'] = otp
    return jsonify({'otp': otp})

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    user_otp = request.json.get('otp')
    saved_otp = session.get('otp')
    if user_otp == saved_otp:
        return jsonify({"message": "2FA successful!"})
    return jsonify({"message": "Invalid OTP"}), 401

if __name__ == '__main__':
    app.run(debug=True)
