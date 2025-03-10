from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class RegisterForm(FlaskForm):
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
