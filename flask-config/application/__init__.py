from flask import Flask
app = Flask(__name__)

from application import views
from application import admin_views
def create_app():
    if app.config["ENV"] == "production":
        app.config.from_object("config.Production")
    else:
        app.config.from_object("config.Development")

    return app