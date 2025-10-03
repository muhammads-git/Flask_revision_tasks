from flask import Flask,render_template,redirect,url_for,flash,get_flashed_messages
from dotenv import load_dotenv
from form import RegistrationForm

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] ='abcdefghi'

@app.route('/')
def basic():
   register_form = RegistrationForm()
   return render_template('registerroute.html',register_form=register_form)

@app.route('/register',methods=['POST','GET'])
def registerform():
   register_form = RegistrationForm()
   if register_form.validate_on_submit():
      name = register_form.name.data
      password = register_form.password.data
      email = register_form.email.data
      confirm_password = register_form.confirm_password.data

      # message
      flash('Data has been saved','success')
   return render_template('thanks.html',register_form=register_form)


if __name__ == "__main__":
   app.run(debug=True)
