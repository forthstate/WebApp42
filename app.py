from flask import Flask, render_template, request, redirect

# Configure Flask application
app = Flask(__name__)

# Landing page
@app.route("/")
def index():
	return render_template("index.html")