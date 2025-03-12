from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise validators.ValidationError("Username already exists !")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data).first()
        if email_address:
            raise validators.ValidationError("Email address already exists !")

    username = StringField(label='User Name:',
                           validators=[
                               validators.Length(min=2, max=30),
                               validators.DataRequired()
                           ])
    email_address = StringField(label='Email Address:',
                                validators=[
                                    validators.Email(),
                                    validators.DataRequired()
                                ])
    password1 = PasswordField(label='Password:',
                              validators=[
                                  validators.Length(min=6),
                                  validators.DataRequired()
                              ])
    password2 = PasswordField(label='Confirm Password:',
                              validators=[
                                  validators.EqualTo('password1'),
                                  validators.DataRequired()
                              ])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:',
                           validators=[
                               validators.DataRequired()
                           ])

    password = PasswordField(label='Password:',
                             validators=[
                                 validators.DataRequired()
                             ])

    submit = SubmitField(label='Login')
