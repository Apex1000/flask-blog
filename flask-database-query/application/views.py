from flask import render_template,request,redirect
from application import app
from .models import db, Todos
@app.route('/')
def index():
    print(app.config)
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
tasks = []
@app.route("/todo", methods=["GET","POST"])
def todo():
    if (request.method == "POST"):
      value = request.form["task"]
      new_todo = Todos(todo = value)
      db.session.add(new_todo)  # Adds new Todo record to database
      db.session.commit()
      return redirect('todo')
    todos = Todos.query.all() # To render all the todo 
    return render_template("public/main/todo.html",todos=todos)

@app.route('/signin/<username>')
def signin(username):
  return render_template("public/main/signin.html",username=username)

@app.route("/multiple/<name>/<age>/<country>")
def multiple(name,age,country):
	return render_template("public/main/multipal.html",name=name,age=age,country=country)

@app.route('/todo/<task>')
def todos(task):
  todos = Todos.query.get(task) # To render all the todo  # Commits all changes
  return "<p> Your task "+task+" is "+todos.todo+"</h1>"
