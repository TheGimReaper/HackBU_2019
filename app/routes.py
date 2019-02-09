from flask import render_template, flash, redirect, url_for
from app.forms import UserForm
from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = UserForm()
	
	if form.validate_on_submit():
		return redirect(url_for('index'))

	return render_template('index.html', form=form)
