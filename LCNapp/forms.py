from wtforms.fields.html5 import DateField
import phonenumbers
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, PasswordField, DateField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo, Optional,  NumberRange


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


class MemberUpdate(Form):
    """Member update form"""
    fName = StringField(
        'First Name',
        validators=[DataRequired()])
    lName = StringField(
        'Last Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[Optional()])
    email = StringField("Email", validators=[DataRequired(),
                                             Email(message=(u'Little short for an email address?'))])
    dob = DateField('Birthday', format='%m/%d/%Y', validators=[Optional()])

    submit = SubmitField('Submit Changes')


class ChangePassword(Form):
    """Change Member Password"""
    old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=8, message='Password is too short')
                                                             ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password is too short')
                                                     ])
    pass_confirm = PasswordField('Confirm Password', validators=[EqualTo('password',
                                                                         message=(u'passwords must match'))])
    change = SubmitField('Change Password')


class MemberSecarchDob(Form):
    """Search for members by birth month form"""
    dob = DateField('Birthday Month', format='%m', validators=[Optional()])

    search1 = SubmitField('Birthday Month Search')


class MemberSearchName(Form):
    """Search for members by last name form"""
    lName = StringField(
        'Last Name', validators=[DataRequired()])
    search2 = SubmitField('Last Name Search')


class MemberSearchByRegister(Form):
    """List memebers my registratin date form"""
    search3 = SubmitField('List Members by Registration Date')


class MemberEmailExport(Form):
    """Form to export emails"""
    exp_email = SubmitField('Export Emails')
