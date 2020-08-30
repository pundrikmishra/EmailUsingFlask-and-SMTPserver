from flask import Flask
from flask_mail import Mail, Message
import config

app = Flask(__name__)
# app.config.update(
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT=465,
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME=config.MAIL_USERNAME,
#     MAIL_PASSWORD=config.MAIL_PASSWORD
# )
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] =
app.config['MAIL_USE_SSL'] = True  # also if you write 465 instead of True then also work
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
# app.config['MAIL_DEFAULT_SENDER'] = 'xyz@gmail.com'
# app.config['MAIL_DEBUG'] = app.debug
# app.config['MAIL_MAX_EMAILS'] =
# app.config['MAIL_SUPPRESS_SEND'] =
# app.config['MAIL_ASCII_ATTACHMENTS'] =
mail = Mail(app)
name = 'kaju'

@app.route("/")
def index():
    msg = Message("Hello " +name, body='kashyap mishra', html='Pundrik Mishra', sender='xyz@gmail.com', recipients=['xyz@gmail.com']) #always remember like recipients, sender email is not wrritten under [] ....
    # msg = Message("Hello",sender=['xyz@gmail.com'], recipients=['xyz@gmail.com']) # Not do like this, sender email is not wrritten under squre bracket
    # msg.body = 'pundrik mishra'
    # msg.html = "<b> pm km</b>"
    # msg.subject = 'kashyap mishra'
    mail.send(msg)
    return "message sent"
    # mail.send_message("Hello", sender=['xyz@gmail.com'], recipients=['xyz@gmail.com'])
    # return "message sent"



if __name__ == '__main__':
    app.run(debug=True)
