from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(dir_path+'/../Model')

from middle import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "hush"

#@app.route('/search')
def search(time,preference,page=None,category=None,domains=None,froms=None,to=None,language='en',sort_by=None,country=None):
	searchDic = {}
	searchDic['q'] = preference
	searchDic['page'] = page
	searchDic['category'] = category
	searchDic['domains'] = domains
	searchDic['from'] = froms
	searchDic['to'] = to
	searchDic['country'] = country
	searchDic['language'] = language
	searchDic['sort_by'] = sort_by
	return json.dumps(getPreference(searchDic,time))

class UserForm(Form):
	r_time = IntegerField('Desired Read Time', validators=[NumberRange(min=1)])

	topic = StringField('Desired Keyword', validators=[InputRequired()])

@app.route('/', methods=['GET','POST'])
def index():
	form = UserForm()
	if form.validate_on_submit():
		flash('Read time entered {}, topic={}'.format(form.r_time.data, form.topic.data))
		return search(form.r_time.data, form.topic.data)
	return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
