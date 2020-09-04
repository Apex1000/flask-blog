from application import app

@app.route('/')
def index():
    return "Index Page"

@app.route('/about')
def about():
    return "About Page"

@app.route('/blog')
def iblog():
    return "Blog Page"