from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = "hush"

class UserForm(Form):
	r_time = IntegerField('Desired Read Time', validators=[NumberRange(min=1)])

	topic = StringField('Desired Keyword', validators=[InputRequired()])


@app.route('/', methods=['GET','POST'])
def index():
	form = UserForm()
	if form.validate_on_submit():
		flash('Read time entered {}, topic={}'.format(form.r_time.data, form.topic.data))
		return ("%d, %s" %(form.r_time.data, form.topic.data))
	return render_template('index.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)