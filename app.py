from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        customer = request.form["name"]
        project = request.form["project"]
        rating = request.form["rating"]
        feedback = request.form["feedback"]
        # print(customer, dealer, rating, feedback)
        if customer == "" or project == "":
            return render_template("index.html", message="Please enter required data.")
        return render_template("success.html")

if __name__ == "__main__":
    app.debug = True
    app.run()