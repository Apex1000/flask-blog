from flask import render_template
from application import app

@app.route('/')
def index():
    return render_template('public/main/index.html',
                            title="Flask Application")
@app.route('/about')
def about():
    return render_template('public/main/about.html')

@app.route('/blog')
def iblog():
    return render_template('public/main/blog.html')