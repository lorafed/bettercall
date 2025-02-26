import time
import random

# Mock Donor Data
donor_data = {
    "001": {"name": "John Doe", "phone": "+1234567890", "timezone": "PST", "history": "High School Program"},
    "002": {"name": "Jane Smith", "phone": "+0987654321", "timezone": "EST", "history": "Alumni Donor"},
}

# Mock Call Functions
def make_call(donor):
    print(f"Dialing {donor['name']}...")
    time.sleep(2)
    if random.choice([True, False]):  # Simulating a bot block
        print("Blocked by caller bot. Retrying...")
        bypass_caller_bot(donor)
    else:
        print(f"Connected to {donor['name']}. Conversation successful.")
        adjust_audio()
        handle_call_options(donor)

def bypass_caller_bot(donor):
    print(f"Attempting to bypass caller bot for {donor['name']}...")
    time.sleep(2)
    print(f"Bypassed successfully. Connected to {donor['name']}.")
    adjust_audio()
    handle_call_options(donor)

def adjust_audio():
    volume = 5  # Default volume
    while True:
        print(f"Current volume: {volume} (1-10)")
        action = input("Would you like to (u)p or (d)own the volume, or (m)ute the call sound? ")
        if action == 'u' and volume < 10:
            volume += 1
        elif action == 'd' and volume > 0:
            volume -= 1
        elif action == 'm':
            print("Call sound muted.")
            break
        else:
            print("Invalid input or volume already at maximum/minimum.")
        print(f"Volume set to: {volume}")
        if input("Continue adjusting volume? (y/n) ") != 'y':
            break

def handle_call_options(donor):
    options = """
    1. Leave a message on the Answering Machine
    2. Log Call Outcome
    3. Send Follow-Up Email/Text
    4. End Call
    """
    while True:
        print(options)
        choice = input("Choose an option: ")
        if choice == "1":
            print(f"Leaving a message for {donor['name']}...")
        elif choice == "2":
            print(f"Logging call outcome for {donor['name']}...")
        elif choice == "3":
            send_follow_up(donor)
        elif choice == "4":
            print("Call ended.")
            break
        else:
            print("Invalid option.")

def send_follow_up(donor):
    print(f"Preparing to send a follow-up email/text to {donor['name']}.")
    # Allowing full customization
    body = input("Enter the full body of your message: ")
    print(f"Message to {donor['name']}: {body}")
    if input("Send the message? (y/n) ") == 'y':
        print("Message sent successfully.")
    else:
        print("Message not sent.")

# Navigation
def main_menu():
    while True:
        print("Main Menu:\n1. Call a Donor\n2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            donor_id = input("Enter Donor ID: ")
            if donor_id in donor_data:
                make_call(donor_data[donor_id])
            else:
                print("Invalid Donor ID.")
        elif choice == "2":
            print("Exiting the app.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
