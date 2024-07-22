"""
AUTH BLUEPRINT
auth/__init__.py
Defines the auth blueprint and imports the auth_routes module.
"""

from flask import Blueprint

bp = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/auth/static/'
)

# Import auth_routes.py
from . import auth_routes