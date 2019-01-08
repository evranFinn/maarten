from flask import render_template, flash, url_for, redirect, request, g
from flask_mail import Mail, Message
from flask_babel import _, get_locale
from app import app
from app.forms import ContactForm

@app.before_request
def before_request():
    g.locale = str(get_locale())

mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = 1
app.config["MAIL_USERNAME"] = 'januaryinrome@gmail.com'
app.config["MAIL_PASSWORD"] = '{aRH+jMZwq<5ST/B'

mail.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title=_('Maarten van Norden, composer and musician'))

@app.route('/biografie')
def biografie():
    return render_template('biografie.html', title=_('Biography Maarten van Norden'))

@app.route('/compositie')
def compositie():
    return render_template('compositie.html', title=_('Maarten van Norden, compositions'))

@app.route('/publicatie')
def publicatie():
    return render_template('publicatie.html', title=_('Maarten van Norden, publications'))

@app.route('/event')
def event():
    return render_template('event.html', title=_('events Maarten van Norden'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  if form.validate_on_submit():
      msg = Message(subject='your website received a contact request', sender='lupoolandese@gmail.com', recipients=['jan@rubsaam.nl'])
      msg.body = """
      From: %s <%s> tel.:%s
      %s
      """ % (form.name.data, form.email.data, form.telephone.data, form.message.data)
      mail.send(msg)

      flash(_('Your message is sent. I will contact you soon.'))
      return redirect('/index')
  return render_template('contact.html', title='Contact', form=form)
