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

@app.route('/variable')
def variable():
    my_name = "xyz"
    listname = ["Tom","Jarry","Oggy","cockroaches"]
    prise = {
    "water": 20,
    "colddrink": 30,
    "softdrink": 25,
    "mango": 20,
    "nuts": 34
		}
    numbers = [1,2,3,4,5,6,7,8,9,10]

    return render_template('public/main/variable.html',
                            name =my_name,
                            listname =listname,
                            prises =prise,
                            numbers =numbers)