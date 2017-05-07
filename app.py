from flask import Flask, redirect, url_for, request, render_template
from flask_mail import Mail, Message
import os
import json
app = Flask(__name__)


@app.route('/<name>')
def main(name):
    return render_template('test.html', name=name)


@app.route('/mail', methods=['POST'])
def mail():
	app.config['MAIL_SERVER']='smtp.gmail.com'
	app.config['MAIL_PORT'] = 587      #465 for SSL
	app.config['MAIL_USE_TLS'] = True
	app.config['MAIL_USE_SSL']=  False #True
	app.config['MAIL_USERNAME'] = 'dibyadasiscool@gmail.com'
	app.config['MAIL_PASSWORD'] = 'samsunghp'
	mail = Mail(app)
	form_data = request.form['msg']
	sender_name = request.form['name']
	sender_email = str(request.form['email'])
	msg = Message('Query',sender = 'dibyadasiscool@gmail.com', recipients = ['dibyadas998@gmail.com'])
	msg.body = form_data
	mail.send(msg)
	msg_user = Message("KOSS:query recieved will be responded soon",sender = 'dibyadasiscool@gmail.com', recipients = [sender_email])
	msg_user.body = "Hi "+sender_name+" ,\n\n"+"Your message has been recieved by us and we will responded to it soon."+"\nThank-you for communicating with us hope your query will cleared by our team."+"\n\n\nKOSS IIT Khragpur"
	mail.send(msg_user)
	return ("sent",200,{'Access-Control-Allow-Origin':'*'})

# if __name__ == "__main__":  # This is for local testin
#     app.run(host='localhost', port=3453, debug=True)

if __name__ == "__main__":  # This will come in use when
    port = int(os.environ.get("PORT", 5000))  # the app is deployed on heroku
    app.run(host='0.0.0.0', port=port)
