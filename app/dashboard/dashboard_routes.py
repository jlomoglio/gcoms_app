"""
dashboard_routes.py
This file contains all the routes that are
associated with the dashboard blueprint.
"""

from app.dashboard import bp
from flask import render_template
from flask_login import login_required, current_user

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)