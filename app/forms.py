from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_babel import _, lazy_gettext as _l


class ContactForm(FlaskForm):
  name = TextField(_l('Name'), validators=[DataRequired(_l('Please enter your name.'))])
  email = TextField(_l('Email'), validators=[DataRequired(_l('Please enter your email address.')), Email(_l('Please enter a valid email address.'))])
  telephone = TextField(_l('Phone Number, optional'))
  message = TextAreaField(_l('Message'), validators=[DataRequired(_l('Please enter a message'))])
  submit = SubmitField(_l('Send'))
