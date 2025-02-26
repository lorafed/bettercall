# BetterCall

## A modern, efficient, and user-friendly fundraising call center application

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/lorafed/bettercall)

---

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Security Features](#security-features)
- [Background Tasks](#background-tasks)
- [Real-Time Updates](#real-time-updates)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## **Introduction**
BetterCall is a **modern fundraising call center application** that improves upon existing solutions by eliminating inefficiencies, improving the UI, and adding essential features like:
- Simplified navigation
- Call bot bypass
- Personalization tools
- Audio controls
- Real-time notifications
- Secure authentication
- Automated follow-ups

This project is intended for **universities, nonprofits, and organizations** that rely on donor engagement via phone, email, and SMS.

---

## **Features**
### **🚀 Core Functionalities**
✔ **Intuitive UI & Navigation** – Reduced unnecessary clicks and improved user experience  
✔ **Caller Bot Bypass** – Enables connection through spam filters like Nomorobo  
✔ **Advanced Personalization** – Fully customizable email and text templates  
✔ **Real-Time Notifications** – WebSocket-powered updates for call events  
✔ **Rate-Limiting & Security** – Protects against abuse with API request throttling  
✔ **Automated Follow-Ups** – Email/SMS scheduling for missed or interested donors  
✔ **Data & Reporting** – Interactive dashboards, donation trends, and exportable reports  
✔ **Background Task Processing** – Celery-powered async tasks for reporting & reminders  
✔ **OAuth & Multi-Factor Authentication** – Secure user logins with social accounts  

---

## **Technologies Used**
| **Technology**  | **Purpose** |
|----------------|------------|
| **Python** | Backend logic |
| **Flask** | Web framework |
| **Flask-SQLAlchemy** | ORM for database interactions |
| **SQLite / PostgreSQL** | Database storage |
| **Flask-RESTful** | REST API design |
| **Flask-SocketIO** | Real-time notifications |
| **Flask-Limiter** | Rate limiting |
| **Flask-Login & Flask-Dance** | Authentication (OAuth, JWT) |
| **Celery & Redis** | Background task processing |
| **Twilio API** | SMS and call handling |
| **Flask-Mail** | Email notifications |
| **Plotly/Dash** | Data visualization & reports |
| **pytest** | Automated testing |
| **Docker** | Containerized deployment |

---

## **Installation**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/lorafed/bettercall.git
cd bettercall
```

### **2️⃣ Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set up the database**
```bash
flask db upgrade
```

### **5️⃣ Run the Flask application**
```bash
flask run
```
The app should now be running at **http://127.0.0.1:5000/** 🎉

---

## **Configuration**
### **Environment Variables**
Create a `.env` file and add the following variables:
```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///fundraising.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_password
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```

---

## **Usage**
### **Making Calls**
1. Log in to the app  
2. Navigate to the **Call List**  
3. Click on a donor and press **Start Call**  
4. If blocked by a spam filter, retry with **Caller Bot Bypass**  

### **Logging Call Outcomes**
1. Select **Answering Machine, Successful, Pledge, or No Answer**  
2. Add notes about the call  
3. Send an automated follow-up (SMS/Email)  

### **Generating Reports**
- Navigate to **Reports Dashboard**  
- View real-time donor engagement graphs  
- Export reports in **PDF, CSV, or Excel**  

---

## **API Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/login` | Authenticates user |
| `GET` | `/api/donors` | Fetches donor list |
| `POST` | `/api/call` | Initiates a call |
| `POST` | `/api/follow-up` | Sends follow-up SMS/email |
| `GET` | `/api/reports` | Fetches fundraising stats |

---

## **Security Features**
🔐 **JWT Authentication** – Secure user logins & token expiration  
🔐 **Two-Factor Authentication** – TOTP-based security for accounts  
🔐 **Role-Based Access Control (RBAC)** – Restricts user actions  
🔐 **Rate Limiting** – Prevents brute-force attacks  
🔐 **Data Encryption** – Protects donor info in storage & transit  

---

## **Background Tasks**
BetterCall uses **Celery + Redis** to offload long-running tasks, including:
- Sending bulk emails/SMS follow-ups  
- Weekly fundraising performance reports  
- Database backups & maintenance  

To run Celery:
```bash
celery -A app.celery worker --loglevel=info
```

---

## **Contributing**
We welcome contributions! To contribute:
1. Fork the repo  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added feature"`)  
4. Push to your fork (`git push origin feature-name`)  
5. Submit a pull request  

---

## **License**
📜 **MIT License** – See [LICENSE](LICENSE) for details.

---

## **Contact**
👨‍💻 **Maintainer:** Federico Lora  
📩 **Email:** lora.fed.03@gmail.com  
🔗 **GitHub:** [lorafed](https://github.com/lorafed)  

---

