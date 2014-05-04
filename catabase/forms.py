from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
	name = TextField("Name", [validators.Required("Please enter your name.")])
	email = TextField("Email", [validators.Required("Please enter your email address."), validators.email()])
	subject = TextField("Subject", [validators.Required("Please enter a subject line.")])
	message = TextAreaField("Message", [validators.Required("Please enter a message.")])
	submit = SubmitField("Send")