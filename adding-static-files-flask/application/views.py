from flask import render_template
from application import app

@app.route('/')
def index():
    return render_template('public/index.html')
@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/blog')
def iblog():
    return render_template('public/blog.html')