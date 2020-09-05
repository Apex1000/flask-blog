from application import app
from flask import render_template
@app.route('/admin/dashboard')
def admin():
    return render_template('admin/dashboard.html')