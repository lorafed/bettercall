from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

# Set your secret key. Remember to switch to your live secret key in production!
stripe.api_key = 'your_stripe_secret_key'

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/charge', methods=['POST'])
def charge():
    amount = int(request.form['amount']) * 100  # Amount in cents

    customer = stripe.Customer.create(
        email=request.form['email'],
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Donation'
    )

    return render_template('charge.html', amount=amount/100)

if __name__ == '__main__':
    app.run(debug=True)
