from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = "dev"

if ENV == "dev":
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Hola@migo@localhost/feedback" 
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "" 
    
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), unique=True)
    project = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text())
    
    def __init__(self, user, project, rating, feedback):
        self.user = user
        self.project = project
        self.rating = rating
        self.feedback = feedback
        
    

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
    app.run()