from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, TextField, SelectField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):

	time = IntegerField('Available Reading Time', validators=[DataRequired()])

	topic = SelectField('Topics', choices = ['news','other'], validators = [DataRequired()])

	submit = SubmitField()
	