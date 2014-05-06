from catabase import app
from flask import render_template, request, flash
from forms import ContactForm, AuthForm
from flask.ext.mail import Message, Mail
from models import db

mail = Mail()

# routes to errors

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# routes to pages

@app.route('/', methods=['GET', 'POST'])
def home():
	form = AuthForm()
	if request.method == 'GET':
		return render_template('home.html', form=form)	

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return 'It works.'
	else:
		return 'Something is broken.'

@app.route('/browse')
def browse():
	return render_template('browse.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required!')
			return render_template('contact.html', form=form)
		else:
			msg = Message(form.subject.data, sender = 'tester@rioht.com',recipients=['davecha@gmail.com'])
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)

			return render_template('contact.html', success=True)

	elif request.method == 'GET':
		return render_template('contact.html', form=form)	
