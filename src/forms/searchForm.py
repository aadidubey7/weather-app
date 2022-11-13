from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField(label='Search:', validators=[DataRequired()])
    submit = SubmitField(label='Search')