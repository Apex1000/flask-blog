from application import app

@app.route('/admin/dashboard')
def admin():
    return "Welcome Admin"