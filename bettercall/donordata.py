from flask import Flask, jsonify

app = Flask(__name__)

# Example donor data
donor_data = {
    1: {"name": "John Doe", "phone": "+1234567890", "timezone": "PST", "history": "High School Program"},
    2: {"name": "Jane Smith", "phone": "+0987654321", "timezone": "EST", "history": "Alumni Donor"},
}

@app.route('/api/donors', methods=['GET'])
def get_donors():
    return jsonify(donor_data)

@app.route('/api/donors/<int:donor_id>', methods=['GET'])
def get_donor(donor_id):
    donor = donor_data.get(donor_id)
    if donor:
        return jsonify(donor)
    else:
        return jsonify({'error': 'Donor not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
