from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def login():
    return render_template("index.html")
@app.route("/Signup")
def signup():
    return render_template("Signup.html")
if __name__ == "__main__":
    app.run(debug=True)