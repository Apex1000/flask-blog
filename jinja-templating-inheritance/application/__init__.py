from flask import Flask

app = Flask(__name__,template_folder='templates')

from application import views
from application import admin_views