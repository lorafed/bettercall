from twilio.rest import Client

# Twilio account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

def send_sms(to, body):
    message = client.messages.create(
        body=body,
        from_='+1234567890',  # Your Twilio phone number
        to=to
    )
    print(f'Message sent: {message.sid}')

# Example usage
send_sms('+0987654321', 'Thank you for your donation!')
