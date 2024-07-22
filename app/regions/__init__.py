"""
regions/__init__.py
This file is the entry point of the application.
It creates the Flask app and registers the blueprints.
"""

from flask import Blueprint

bp = Blueprint(
    'regions',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/regions/static/'
)

# Import region_routes.py
from . import region_routes