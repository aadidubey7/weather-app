from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from models.user import UserModel

class UserRegistrationForm(FlaskForm):
    
    def validate_username(self, username):
        if UserModel.find_by_username(username.data):
            raise ValidationError("Username is already exists! Please try with a different username.")

    def validate_email(self, email):
        if UserModel.find_by_email(email.data):
            raise ValidationError("Email is already exists! Please try with a different email address.")
    
    username = StringField(label='User Name:', validators=[DataRequired(), Length(min=2, max=30)])
    email = EmailField(label='Email Address:', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Register')
    
    
class UserLoginForm(FlaskForm):
    email = EmailField(label='Email Address:', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField(label='Register')