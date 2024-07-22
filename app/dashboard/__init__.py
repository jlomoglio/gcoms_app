"""
dashboard/__init__.py
This file is the entry point of the application.
It creates the Flask app and registers the blueprints.
"""

from flask import Blueprint

bp = Blueprint(
    'dashboard',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Import dashboard_routes.py
from . import dashboard_routes