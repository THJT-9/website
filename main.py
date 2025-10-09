from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)


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
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, gmail_app_password)
            connection.sendmail(from_addr=my_email, to_addrs=rec_email,
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
