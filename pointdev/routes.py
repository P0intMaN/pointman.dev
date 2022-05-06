from flask import render_template
from pointdev import app

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/tags') 
def tags():
    return render_template('tags.html')

@app.route('/blogs') 
def blogs():
    return render_template('blogs.html')

@app.route('/join') 
def join():
    return render_template('home.html')

@app.route('/store') 
def store():
    return render_template('home.html')

@app.route('/page1') 
def pages():
    return render_template('page1.html')
