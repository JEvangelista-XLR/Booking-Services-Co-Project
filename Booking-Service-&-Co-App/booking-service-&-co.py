import os
from flask import  Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def home_page():
    return render_template("frontendlanding.html")


if __name__ == "__main__":
    app.run(debug=True)
