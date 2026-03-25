import os
from flask import  Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def home_page():
    return render_template("frontendlanding.html")

@app.get("/about")
def about_page():
    return render_template("aboutpage.html")

@app.get("/contacts")
def contacts_page():
    return render_template("contactspage.html")

if __name__ == "__main__":
    app.run(debug=True)
