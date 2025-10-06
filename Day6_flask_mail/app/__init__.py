from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
from flask_mail import Mail


# initialize flask-bcrypt
bcrypt = Bcrypt()
# initialize mysql create instance 
mysql = MySQL()
# creating mail instance
mail = Mail()


def create_app():
   app = Flask(__name__)
   
   #load environment variable with loadenv()
   load_dotenv()

   # db configurations
   app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
   app.config['MYSQL_HOST']=os.getenv('DB_HOST')
   app.config['MYSQL_USER']=os.getenv('DB_USER')
   app.config['MYSQL_PASSWORD']=os.getenv('DB_PASSWORD')
   app.config['MYSQL_DB']=os.getenv('DB_NAME')
   # flask mail configurations
   app.config['MAIL_SERVER'] = 'smtp.@gmail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USERNAME'] = 'Muhammad Hammad'
   app.config['MAIL_PASSWORD'] = 'nfis ntse ibra tujv'
   app.config['MAIL_DEFAULT_SENDER'] = 'sirhammad760@gmail.com'

   mysql.init_app(app)
   bcrypt.init_app(app)
   mail.init_app(app)


   from app.auths.routes import auth_bp
   from app.errors.errorhandler import error_bp
   # register auth blueprint at root so '/' serves the registration page
   # previously mounted at '/auths' which required visiting '/auths/'
   app.register_blueprint(auth_bp)
   app.register_blueprint(error_bp)

   return app