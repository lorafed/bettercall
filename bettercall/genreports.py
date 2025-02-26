from flask import Flask, render_template, make_response
from fpdf import FPDF

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Donation Report', ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_donation(self, donor_name, amount):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Donor: {donor_name} - Amount: ${amount}', ln=True)

@app.route('/generate
