try:
    from app import db as db
except ImportError:
    from __name__ import db


class Region(db.Model):
    reg_id = db.Column(db.Integer, primary_key=True)
    reg_name = db.Column(db.String(100), nullable=False)
    reg_description = db.Column(db.String(200), nullable=False)
    reg_image = db.Column(db.String(200), nullable=False)
    reg_manager = db.Column(db.String(200), nullable=False)
    reg_manager_phone = db.Column(db.String(50), nullable=False)
    reg_manager_email = db.Column(db.String(100), nullable=False)
    reg_lat = db.Column(db.String(250), nullable=False)
    reg_lng = db.Column(db.String(250), nullable=False)
    reg_continent = db.Column(db.String(100), nullable=False)
    reg_country = db.Column(db.String(100), nullable=False)
    reg_state = db.Column(db.String(100), nullable=False)
    reg_city = db.Column(db.String(100), nullable=False)
    reg_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Region {self.reg_name}>'


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state_id = db.Column(db.Integer(), nullable=False)
    state_code = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer(), nullable=False)
    country_code = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.String(250), nullable=False)
    longitude = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<City {self.name}>'

