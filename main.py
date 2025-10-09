import os
from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_EMAIL_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")
REC_EMAIL = os.environ.get("REC_EMAIL")
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/certificate')
def certificate():
    return render_template("certificate.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=REC_EMAIL,
                                msg=f"Subject: New Message Received!\n\n"
                                    f"Name: {username}\n"
                                    f"Email: {email}\n"
                                    f"Phone: {phone}\n"
                                    f"Message: {message}"
            )
        return render_template("contact.html", message="Message sent!")
    else:
        return render_template("contact.html", message="")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
