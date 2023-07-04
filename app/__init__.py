from flask import Flask

app = Flask(__name__)

# Routes
from app import admin_views
from app import views
