from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

donations = []

class Donation(Resource):
    def get(self, donation_id):
        for donation in donations:
            if donation['id'] == donation_id:
                return donation
        return {'message': 'Donation not found'}, 404

    def post(self):
        donation = {
            'id': len(donations) + 1,
            'name': request.json['name'],
            'amount': request.json['amount']
        }
        donations.append(donation)
        return donation, 201

api.add_resource(Donation, '/donation', '/donation/<int:donation_id>')

if __name__ == '__main__':
    app.run(debug=True)
