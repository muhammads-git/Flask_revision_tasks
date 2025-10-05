from flask import Flask,render_template,redirect,url_for,flash,get_flashed_messages
from app import mysql   #import the objects
from flask import Blueprint
from app.forms.form import RegisterForm
from app import bcrypt



# create a Blueprint instance
auth_bp = Blueprint('auth_bp',__name__,template_folder='templates')

@auth_bp.route('/')
def home():
   form=RegisterForm()
   return render_template('register.html',form=form)

@auth_bp.route('/register',methods=['POST'])
def register():
   form = RegisterForm()
   if form.validate_on_submit():
      username = form.name.data
      password = form.password.data
      email = form.email.data
      
      # hash the password
      hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

      # open db and insert data in it
      cur = mysql.connection.cursor()

      # execute the query
      cur.execute('INSERT INTO users (name,password,email) VALUES (%s,%s,%s)',(username,hashed_password,email))

      # commit 
      mysql.connection.commit()

      #close 
      cur.close()
      
   return render_template('thanks.html',form=form)





