🛡️ reCAPTCHA Implementation using HTML and Python


📖 Overview
This repository contains a simple implementation of Google's reCAPTCHA using HTML and Python. reCAPTCHA helps protect websites from spam and abuse by using advanced risk analysis techniques to distinguish between humans and bots.

✨ Features
User-friendly Interface: A clean and simple HTML form integrated with reCAPTCHA. 🖥️
Backend Verification: Python script to handle the reCAPTCHA verification process. 🐍
Security: Ensures only human users can submit the form, protecting your website from bots. 🛡️
🛠️ Requirements
Python 3.x
Flask
Requests library
📦 Installation
Clone the repository:

sh

git clone https://github.com/prajes_das/recaptcha-implementation.git
cd recaptcha-implementation
Install dependencies:

sh

pip install flask requests
Obtain reCAPTCHA API keys:

Go to the reCAPTCHA admin console 🌐.
Register your site and obtain the site key and secret key 🔑.
Configure the keys:

Open app.py and replace the placeholders with your actual site key and secret key.
python

RECAPTCHA_SITE_KEY = 'your-site-key'
RECAPTCHA_SECRET_KEY = 'your-secret-key'
🚀 Usage
Run the Flask application:

sh

python app.py
Access the application:

Open your web browser and navigate to http://127.0.0.1:5000 🌍.
Fill out the form and complete the reCAPTCHA challenge to test the implementation.
🗂️ File Structure

recaptcha-implementation/
├── templates/
│   └── index.html
├── app.py
└── README.md
templates/index.html: Contains the HTML form with reCAPTCHA.
app.py: Flask application to handle form submission and reCAPTCHA verification.
README.md: Project documentation.
📝 Code Explanation
HTML Form (index.html)
html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>reCAPTCHA Example</title>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
</head>
<body>
    <form action="/" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <div class="g-recaptcha" data-sitekey="your-site-key"></div>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
Flask Application (app.py)
python
Copy code
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

RECAPTCHA_SITE_KEY = 'your-site-key'
RECAPTCHA_SECRET_KEY = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recaptcha_response = request.form['g-recaptcha-response']
        data = {
            'secret': RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            return 'Verification successful. You are a human! 🎉'
        else:
            return 'Verification failed. Please try again. ❌'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
![image](https://github.com/user-attachments/assets/3fb5145e-7073-4c03-92fe-d7ba9d21f7e4)

