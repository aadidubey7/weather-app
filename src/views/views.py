from flask import render_template, redirect, url_for
from controllers.user import UserController
from controllers.search import SearchController
from forms.userForm import UserRegistrationForm, UserLoginForm
from forms.searchForm import SearchForm
from flask_login import login_user, logout_user, login_required

def home():
    return render_template("home.html")

@login_required
def weather():
    search_form = SearchForm()
    status, output = False, []
    if search_form.validate_on_submit():
        status, output = SearchController.get_location_key_by_city(search_form.search.data)
        if status:
            search_controller = SearchController(search_form.search.data, output)
            search_controller.store_searched_data()

    return render_template("weather.html", form=search_form, status=status, data=output)

def register():
    register_form = UserRegistrationForm()
    if register_form.validate_on_submit():
        user_obj = UserController(
            register_form.username.data,
            register_form.email.data,
            register_form.password.data
        )
        user_obj.register()
        return redirect(url_for("home"))

    return render_template('register.html', form=register_form)

def login():
    login_form = UserLoginForm()
    if login_form.validate_on_submit():
        user = UserController.login(login_form.email.data, login_form.password.data)
        if user:
            login_user(user)
            return redirect(url_for("weather"))
        
    return render_template('login.html', form=login_form)

def logout():
    logout_user()
    return redirect(url_for('home'))