from flask import Flask
from views import views
from db import db
from security import bcrypt, login_manager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = '528df95937673f0a8b67aedf'

def create_app():
    with app.app_context():
        db.init_app(app)
        db.create_all()
        
        bcrypt.init_app(app)
        login_manager.init_app(app)
        login_manager.login_view = 'login'

def add_routes():
    app.add_url_rule("/", view_func=views.home)
    app.add_url_rule("/home", view_func=views.home)
    app.add_url_rule("/index", view_func=views.home)

    app.add_url_rule("/weather", view_func=views.weather, methods=["GET", "POST"])
    app.add_url_rule("/register", view_func=views.register, methods=["GET", "POST"])
    app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout)

if __name__ == "__main__":
    create_app()
    add_routes()
    app.run(debug=True)