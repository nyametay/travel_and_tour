from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__file__))

# Ensure "instance" directory exists
instance_dir = os.path.join(basedir, "instance")
os.makedirs(instance_dir, exist_ok=True)

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=10)

# Secret Key
app.config['SECRET_KEY'] = '1567Tay*'

# Database Path
db_path = os.path.join(instance_dir, "data.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db = SQLAlchemy(app)

# Import routes
from data import routes
