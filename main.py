from flask import Flask, render_template, request
import datetime
import smtplib

EMAIL = 'datigerace@yahoo.com'
PASSWORD = 'irclovgwmytvoazb'
todayYear = datetime.datetime.now().year

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', todayYear=todayYear)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', todayYear=todayYear, msg_sent=False)
    elif request.method == 'POST':
        data = request.form
        send_mail(name=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
        return render_template('contact.html', todayYear=todayYear, msg_sent=True)

@app.route('/projects')
def showProjects():
    return render_template('projects.html', todayYear=todayYear)

def send_mail(name, email, phone, message):
    email_message = f'Subject:New Message on your Website\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,
                         password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=email_message,
                            )
        connection.quit()

if __name__ == "__main__":
    app.run(debug=True)