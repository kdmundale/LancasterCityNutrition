from wtforms.fields.html5 import DateField
import phonenumbers
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo, Optional


class LoginForm(Form):
    """Login Form """
    email = StringField("Email", validators=[DataRequired(
        "Please enter your email address."), Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[DataRequired()])

    login = SubmitField('Login')


class ContactForm(Form):
    """Registration form."""
    fName = StringField(
        'First Name',
        validators=[DataRequired()])
    lName = StringField(
        'Last Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[Optional()])
    email = StringField("Email", validators=[DataRequired(),
                                             Email(message=(u'Little short for an email address?'))])
    dob = DateField('Birthday', format='%m/%d/%Y', validators=[Optional()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password is too short')
                                                     ])
    pass_confirm = PasswordField('Confirm Password', validators=[EqualTo('password',
                                                                         message=(u'passwords must match'))
                                                                 ])
    register = SubmitField('Register')
