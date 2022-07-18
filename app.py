from flask import Flask, render_template, redirect, request


app = Flask(__name__)


@app.route('/')
def index():
	"""Landing page of the WebApp"""
	return render_template('index.html')

"""
Lots more to come !!!
"""

@app.route('/tools/age', methods=["GET","POST"])
def age():
	"""Renders page with the age calculator tool"""
	
	if request.method == "POST":
		# For post query
		pass

	else:
		# For get query
		return render_template('tools/age.html')