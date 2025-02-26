import tkinter as tk
from tkinter import messagebox
import random

# Mock Donor Data
donor_data = {
    "001": {"name": "John Doe", "phone": "+1234567890", "timezone": "PST", "history": "High School Program"},
    "002": {"name": "Jane Smith", "phone": "+0987654321", "timezone": "EST", "history": "Alumni Donor"},
}

class FundraisingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fundraising App")
        self.geometry("400x300")
        self.current_volume = 5
        self.create_widgets()

    def create_widgets(self):
        # Main Menu
        self.label = tk.Label(self, text="Fundraising App Main Menu")
        self.label.pack(pady=10)

        self.call_button = tk.Button(self, text="Call a Donor", command=self.call_donor)
        self.call_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=5)

    def call_donor(self):
        donor_id = tk.simpledialog.askstring("Input", "Enter Donor ID:")
        if donor_id in donor_data:
            donor = donor_data[donor_id]
            self.dial_donor(donor)
        else:
            messagebox.showerror("Error", "Invalid Donor ID.")

    def dial_donor(self, donor):
        if random.choice([True, False]):
            self.bypass_caller_bot(donor)
        else:
            self.connected(donor)

    def bypass_caller_bot(self, donor):
        messagebox.showinfo("Caller Bot", f"Attempting to bypass caller bot for {donor['name']}...")
        self.connected(donor)

    def connected(self, donor):
        response = messagebox.askquestion("Connected", f"Connected to {donor['name']}. Adjust volume?")
        if response == 'yes':
            self.adjust_audio()
        self.call_options(donor)

    def adjust_audio(self):
        self.volume_label = tk.Label(self, text=f"Current volume: {self.current_volume} (1-10)")
        self.volume_label.pack(pady=5)
        
        self.volume_up_button = tk.Button(self, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack(pady=2)
        
        self.volume_down_button = tk.Button(self, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack(pady=2)
        
        self.mute_button = tk.Button(self, text="Mute", command=self.mute_audio)
        self.mute_button.pack(pady=2)

    def volume_up(self):
        if self.current_volume < 10:
            self.current_volume += 1
            self.volume_label.config(text=f"Current volume: {self.current_volume} (1-10)")

    def volume_down(self):
        if self.current_volume > 0:
            self.current_volume -= 1
            self.volume_label.config(text=f"Current volume: {self.current_volume} (1-10)")

    def mute_audio(self):
        self.current_volume = 0
        self.volume_label.config(text="Call sound muted.")

    def call_options(self, donor):
        options_window = tk.Toplevel(self)
        options_window.title("Call Options")

        label = tk.Label(options_window, text=f"Options for {donor['name']}:")
        label.pack(pady=10)

        message_button = tk.Button(options_window, text="Leave a Message", command=lambda: self.leave_message(donor))
        message_button.pack(pady=5)

        log_button = tk.Button(options_window, text="Log Call Outcome", command=lambda: self.log_call(donor))
        log_button.pack(pady=5)

        follow_up_button = tk.Button(options_window, text="Send Follow-Up", command=lambda: self.send_follow_up(donor))
        follow_up_button.pack(pady=5)

        end_button = tk.Button(options_window, text="End Call", command=options_window.destroy)
        end_button.pack(pady=5)

    def leave_message(self, donor):
        messagebox.showinfo("Message", f"Leaving a message for {donor['name']}.")

    def log_call(self, donor):
        messagebox.showinfo("Log Call", f"Logging call outcome for {donor['name']}.")

    def send_follow_up(self, donor):
        message = tk.simpledialog.askstring("Follow-Up", f"Compose your message to {donor['name']}:")
        if message:
            messagebox.showinfo("Message Sent", f"Message to {donor['name']}:\n\n{message}")
        else:
            messagebox.showwarning("Cancelled", "Message not sent.")

if __name__ == "__main__":
    app = FundraisingApp()
    app.mainloop()
