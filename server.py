from flask import Flask,render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
import enum
import smtplib
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registerUsers.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__= "Students"
    id: Mapped[int] = mapped_column(db.Integer,primary_key=True)
    firstName: Mapped[str] = mapped_column(db.String(10),nullable=False)
    lastName: Mapped[str] = mapped_column(db.String(10),nullable=False)
    email: Mapped[str] = mapped_column(db.String(140),nullable=False)
    mobileNumber:Mapped[str] = mapped_column(db.String(10),nullable=False)
@app.route("/")
def login():
    return render_template("index.html")
@app.route("/Signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        role = request.form.get("user")
        if(role == "Student"):
            first_name = request.form.get("fname")
            last_name = request.form.get("lname")
            email = request.form.get("mail")
            mobile_number = request.form.get("mobile")
            student = Student(firstName = first_name,
                              lastName = last_name,
                              email = email,
                              mobileNumber = mobile_number)
            db.session.add(student)
            db.session.commit()
    return render_template("Signup.html")
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)