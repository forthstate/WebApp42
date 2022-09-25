from flask import Flask, render_template, request, redirect
from utilities import *

# Configure Flask application
app = Flask(__name__)

# Landing page
@app.route("/")
def index():
	return render_template("index.html")

# BMI tool
@app.route("/tools/bmi", methods=["GET", "POST"])
def bmi():
	# POST
	if request.method == "POST":
		weight_unit = request.form.get("weight_unit")
		weight = float(request.form.get("weight"))
		if weight_unit == "lb":
			weight = pounds_to_kg(weight)
		height_unit = request.form.get("height_unit")
		height = float(request.form.get("height"))
		if height_unit == "cm":
			height = cm_to_m(height)
		elif height_unit == "ft":
			height = ft_to_m(height)
		elif height_unit == "in":
			height = in_to_m(height)
		Result = "{0:.1f}".format(weight/height/height)
		return render_template("bmi.html", condition=True, Result=Result)

	# GET
	else:
		return render_template("bmi.html", condition=False)
