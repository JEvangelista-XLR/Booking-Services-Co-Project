"""Python code for links to webpages within website"""
import os
from flask import  Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/") #"/" sets home page as root page
def home_page(): # home page render
    return render_template("homepageV2.html")

@app.get("/about")
def about_page(): # about page render
    return render_template("aboutpage.html")

@app.get("/contacts")
def contacts_page(): # contacts page render
    return render_template("contactspage.html")

if __name__ == "__main__":
    app.run(debug=True) # TURN OFF DEBUG WHEN LIVE
