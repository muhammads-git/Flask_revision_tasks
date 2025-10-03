from flask_wtf import FlaskForm
from wtforms.validators import Email,EqualTo,Length,DataRequired
from wtforms import SubmitField,StringField,PasswordField,EmailField


class RegistrationForm(FlaskForm):
   name = StringField('Username',validators=[DataRequired(),Length(min=6,max=20)])
   password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
   email = EmailField('Email',validators=[DataRequired(),Email()])
   confirm_password= PasswordField('Confirm Password',validators=[EqualTo(password)])
   submit = SubmitField('Register')