from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# initialize flask-bcrypt
bcrypt = Bcrypt()
# initialize mysql create instance 
mysql = MySQL()

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

   mysql.init_app(app)
   bcrypt.init_app(app)



   from app.auths.routes import auth_bp
   from app.errors.errorhandler import error_bp
   app.register_blueprint(auth_bp,url_prefix='/auths')
   app.register_blueprint(error_bp)

   return app