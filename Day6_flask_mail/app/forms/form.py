from flask_wtf import FlaskForm
from wtforms.validators import Length,Email,DataRequired
from wtforms import StringField,PasswordField,SubmitField,EmailField



# class Register
class RegisterForm(FlaskForm):
   name = StringField('Username',validators=[DataRequired(),Length(min=6,max=20)])
   password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
   email = EmailField('Email',validators=[DataRequired(),Email()])
   submit = SubmitField('Register')

# class Login

# mail 
class MailForm(FlaskForm):
   email = EmailField('Email',validators=[DataRequired(),Email()])
   submit = SubmitField('MailMe')