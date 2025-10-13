from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import base64
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

# Custom Jinja2 filter for base64 encoding
@app.template_filter('b64encode')
def b64encode_filter(data):
    """Encode binary data as base64 for safe HTML embedding."""
    if data is None:
        return ''
    return base64.b64encode(data).decode('utf-8')

# Initialize DB
db = SQLAlchemy(app)

# Import routes
from data import routes
