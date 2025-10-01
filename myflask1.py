from flask import Flask,render_template,redirect,url_for
from dotenv import load_dotenv

# load .env
load_dotenv()

# create app
app = Flask(__name__)

# dashboard
@app.route('/')
def msg():
   return render_template('msg.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/SeeYou')
def SeeYou():
   return render_template('Seeyou.html')

# run flask app
app.run(debug=True)