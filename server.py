from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
import enum
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registerUsers.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id: Mapped[int] = mapped_column(db.Integer,primary_key=True)
    firstName: Mapped[str] = mapped_column(db.String(10),nullable=False)
    lastName: Mapped[str] = mapped_column(db.String(10),nullable=False)
    

@app.route("/")
def login():
    return render_template("index.html")
@app.route("/Signup")
def signup():
    return render_template("Signup.html")
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)