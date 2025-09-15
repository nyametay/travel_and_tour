# 🌍 GlobeTrek Travel & Tour Agency  

A responsive **Travel & Tour Agency web app** built with **Flask, TailwindCSS, and SQLite**.  
It allows users to explore destinations, make bookings, and sends email notifications to guides with booking details.  

---

## 🚀 Features  
- 📱 **Responsive Design** with light & dark mode support  
- 🌐 **Navbar with mobile hamburger menu**  
- 🏝️ **Destinations page** with popular sites  
- 📅 **Booking form** with validation  
- 📧 **Email notifications** sent to multiple guides via Gmail SMTP  
- ⚡ **Flash messages** for feedback  
- 🌓 **Dark/Light theme toggle** (persistent via localStorage)  

---

## 🛠️ Tech Stack  
- **Frontend:** [Tailwind CSS](https://tailwindcss.com/)  
- **Backend:** [Flask](https://flask.palletsprojects.com/)  
- **Database:** SQLite (via SQLAlchemy)  
- **Email Service:** Python `smtplib` with Gmail SMTP  
- **Deployment Ready:** Can be hosted on Render, Heroku, or any WSGI-compatible server  

---

## 📂 Project Structure  

```bash
TravelAgency/
│── static/
│   ├── scripts/
│   │   └── code.js        # Mobile menu + theme toggle logic
│   │   └── notification.js
│── templates/
│   ├── index.html         # Home page
│   ├── header.html        # Navbar & mobile menu
│   ├── destinations.html  # Destinations page
│   └── book_now.html      # Booking form
│── app.py                 # Flask backend
│── models.py              # SQLAlchemy models
│── email_utils.py         # Booking email sender
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

## ⚙️ Installation
- Clone the repository
``` bash
git clone https://github.com/your-username/globetrek-travel.git
cd globetrek-travel
```

- Create a virtual environment
``` bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

- Install dependencies
``` bash
pip install -r requirements.txt
```

- Set environment variables (create .env file)
``` bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_SENDER=your-email@gmail.com
```

- Run the app
```bash
flask run
Now visit 👉 http://127.0.0.1:5000
```
- 📧 Email Notifications
``` bash
When a booking is made, an email is automatically sent to guides:

RECIPIENTS = [
    "guide1@example.com",
    "guide2@example.com",
    "guide3@example.com"
]

```
## Uses Gmail SMTP with App Passwords for secure authentication.

📸 Screenshots
🌞 Light Mode

🌙 Dark Mode

## 🛡️ Security Notes

- Do NOT hardcode your email or password. Use .env files or GitHub secrets.
- Never commit .env or sensitive credentials.

## 🤝 Contributing

- Fork the repo
- Create your feature branch (git checkout -b feature/new-feature)
- Commit changes (git commit -m "Added new feature")
- Push to branch (git push origin feature/new-feature)
- Open a Pull Request 🎉
