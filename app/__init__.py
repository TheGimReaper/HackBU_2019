from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


from app import routes