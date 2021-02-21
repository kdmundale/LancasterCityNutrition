from wtforms.fields.html5 import DateField
import phonenumbers
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, DateField, HiddenField, IntegerField, SelectField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo, Optional,  NumberRange


class LoginForm(FlaskForm):
    """Login Form """
    email = StringField("Email", validators=[DataRequired(
        "Please enter your email address."), Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[DataRequired()])

    login = SubmitField('Login')


class ContactForm(FlaskForm):
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
                                                                         message=('passwords must match'))
                                                                 ])
    register = SubmitField('Register')


class MemberUpdate(FlaskForm):
    """Member update form"""
    fName = StringField(
        'First Name',
        validators=[DataRequired()])
    lName = StringField(
        'Last Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[Optional()])
    email = StringField("Email", validators=[DataRequired(),
                                             Email(message=('Little short for an email address?'))])
    dob = DateField('Birthday', format='%m/%d/%Y', validators=[Optional()])

    submit = SubmitField('Submit Changes')


class ChangePassword(FlaskForm):
    """Change Member Password"""
    old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=8, message='Password is too short')
                                                             ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password is too short')
                                                     ])
    pass_confirm = PasswordField('Confirm Password', validators=[EqualTo('password',
                                                                         message=(u'passwords must match'))])
    change = SubmitField('Change Password')


class MemberSecarchDob(FlaskForm):
    """Search for members by birth month form"""
    dob = DateField('Birthday Month', format='%m', validators=[Optional()])

    search1 = SubmitField('Birthday Month Search')


class MemberSearchName(FlaskForm):
    """Search for members by last name form"""
    lName = StringField(
        'Last Name', validators=[DataRequired()])
    search2 = SubmitField('Last Name Search')


class MemberSearchByRegister(FlaskForm):
    """List memebers my registratin date form"""
    search3 = SubmitField('List Members by Registration Date')


class MemberEmailExport(FlaskForm):
    """Form to export emails"""
    exp_email = SubmitField('Export Emails')


class MakeUnavail(FlaskForm):
    """Make an item unavailable"""
    shake_id1 = StringField('Shake ID', validators=[DataRequired()])
    switch_avail = SubmitField('change')


class MakeAvail(FlaskForm):
    """Make item available"""
    shake_id2 = StringField('Shake ID', validators=[DataRequired()])
    switch_unavail = SubmitField('change')


class AddItem(FlaskForm):
    """Add new item to product menu"""
    item_name = StringField(
        'Item Name', validators=[DataRequired()])
    description = StringField(
        'Description', validators=[DataRequired()])
    group = SelectField(
        'Group #', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], validators=[DataRequired()])
    add_item = SubmitField('Add Item')
