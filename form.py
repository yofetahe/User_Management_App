from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class registrationForm(Form):
    first_name = StringField('First Name: ', validators=[DataRequired("First name is required")])
    last_name = StringField('Last Name: ', validators=[DataRequired("Last name is required")])
    email = StringField('Email: ', validators=[DataRequired("Email is required"), Email("Please enter valid email address")])
    submit = SubmitField('Create')

class userUpdateForm(Form):
    first_name = StringField('First Name: ', validators=[DataRequired("First name is required")])
    last_name = StringField('Last Name: ', validators=[DataRequired("Last name is required")])
    email = StringField('Email: ', validators=[DataRequired("Email is required"), Email("Please enter valid email address")])
    submit = SubmitField('Update')