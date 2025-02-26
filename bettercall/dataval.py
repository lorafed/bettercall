from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

class DonationSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    amount = fields.Float(required=True)

@app.route('/donate', methods=['POST'])
def donate():
    try:
        data = request.json
        schema = DonationSchema()
        result = schema.load(data)
        return jsonify({"message": "Donation processed successfully", "data": result})
    except ValidationError as err:
        return jsonify(err.messages), 400

if __name__ == '__main__':
    app.run(debug=True)
