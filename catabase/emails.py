from flask import render_template
from flask.ext.mail import Message
from routes import mail
from decorators import async

@async

def send_asyc_email(msg):
	mail.send(msg)

def send_email(subject, sender, recipients):
	msg.body = """
		From: %s <%s>
		%s
		""" % (form.name.data, form.email.data, form.message.data)
		mail.send(msg)