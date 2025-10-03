from flask import Flask,render_template,redirect,url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
   return render_template('hello.html')

@app.route("/hi")
def hi():
   return render_template('hi.html')

@app.route("/dashboard")
def dashboard():
   mylist = ["Muhammad","Ali","Usaman"]
   return render_template('dashboard.html',mylist=mylist)


if __name__ == "__main__":
   app.run(debug=True)