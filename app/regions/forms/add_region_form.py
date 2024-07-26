from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField, SelectField, FileField, EmailField, ValidationError
from wtforms.validators import InputRequired, Email
from wtforms_alchemy import PhoneNumberField
import phonenumbers


def validate_phone(form, field):
    if len(field.data) < 10:
        raise ValidationError('Invalid phone number.')

class AddRegionForm(FlaskForm):
    reg_name = StringField('Region Name', validators=[InputRequired()])
    reg_description= TextAreaField('Description', validators=[InputRequired()])
    reg_image = FileField('Image', validators=[InputRequired()])
    reg_manager = StringField('Manager', validators=[InputRequired()])
    reg_manager_phone = PhoneNumberField('Manager Phone', validators=[InputRequired(), validate_phone])

    reg_manager_email = EmailField('Manager Email', validators=[InputRequired(), Email()])
    reg_lat = HiddenField('Latitude')
    reg_lng = HiddenField('Longitude')
    reg_continent = SelectField(
        'Continent',
        choices=[
            ('', 'Select a Continent'),
            ('Africa', 'Africa'),
            ('Asia', 'Asia'),
            ('Europe', 'Europe'),
            ('North America', 'North America'),
            ('South America', 'South America'),
            ('Oceania', 'Oceania')
        ],
        validators=[InputRequired()],
        validate_choice=False
    )
    reg_country = SelectField('Country', validators=[InputRequired()])
    reg_state = SelectField('State', validators=[InputRequired()])
    reg_state_code = HiddenField('State Code', validators=[InputRequired()])
    reg_city = SelectField('City', validators=[InputRequired()])
    reg_type = SelectField(
        'Region Type',
        choices=[
            ('', 'Select a Type'),
            ('Manufacturing', 'Manufacturing'),
            ('Energy', 'Energy'),
            ('Office', 'Office'),
            ('Legacy Center', 'Legacy Center'),
            ('Housing', 'Housing'),
            ('Schools', 'Schools'),
            ('Medical', 'Medical')
        ],
        validators=[InputRequired()])

    reg_submit = SubmitField('Add Region')


