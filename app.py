from flask import Flask, request, render_template, send_file
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import logging


app = Flask(__name__)

SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Access database with SQLAlchemy
db_uri = 'sqlite:///practice.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class Comment(db.Model):

    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.Text())
    comment = db.Column(db.Text())

    def __init__(self, pub_date, name, comment):

        self.pub_date = pub_date
        self.name = name
        self.comment = comment

try:
    db.create_all()
except Exception as e:
    print(e.args)
    pass


@app.route("/")
def index():
    # query.all() means read all
    text = Comment.query.all()
    return render_template("index.html", lines=text)


@app.route("/result", methods=["POST"])
def result():
    # Get date
    date = datetime.now()
    comment = request.form["comment_data"]
    name = request.form["name"]
    # Create data for insert
    comment_data = Comment(pub_date=date, name=name, comment=comment)
    # Insert into table
    db.session.add(comment_data)
    # Save information
    db.session.commit()
    return render_template("result.html", comment=comment, name=name, now=date)

logging.basicConfig(filename='access.log', level=logging.DEBUG)

