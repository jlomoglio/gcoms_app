from app.regions import bp
from flask import render_template, request, flash, redirect, url_for, jsonify, json
from flask_login import login_required, current_user
from .forms.add_region_form import AddRegionForm
from .region_models import Region, City
from app import db

@bp.route('/regions', methods=['GET', 'POST'])
@login_required
def regions():
	# Grab all regions from the database
	regions = Region.query.all()
	return render_template('regions.html', user=current_user, regions=regions)


@bp.route('/regions/map', methods=['GET'])
@login_required
def get_regions_map():
	regions = Region.query.all()
	region_data = []
	for region in regions:
		region_data.append({
			'name': region.reg_name,
			'lat': region.reg_lat,
			'lng': region.reg_lng,
			'state': region.reg_state,
			'city': region.reg_city,
		})

	return region_data


@bp.route('/regions/cards')
@login_required
def get_region_cards():
	regions = Region.query.all()
	return render_template('_region_card.html', regions=regions)



@bp.route('/get_region/<int:id>', methods=['POST'])
@login_required
def get_region():
	# Logic for an existing region

	return render_template('regions.html')


@bp.route('/add_region', methods=['GET', 'POST'])
@login_required
def add_region():
	form = AddRegionForm()

	# Logic for adding a new region
	if request.method == 'POST':
		""" Assign form data to vars """
		reg_name = request.form['reg_name']
		reg_description = request.form['reg_description']
		reg_image = request.form['reg_image']
		reg_manager = request.form['reg_manager']
		reg_manager_phone = request.form['reg_manager_phone']
		reg_manager_email = request.form['reg_manager_email']
		reg_lat = request.form['reg_lat']
		reg_lng = request.form['reg_lng']
		reg_continent = request.form['reg_continent']
		reg_country = request.form['reg_country']
		reg_state = request.form['reg_state']
		reg_city = request.form['reg_city']
		reg_type = request.form['reg_type']

		if reg_lat != '' and reg_lng != '':
			""" Validate form data """
			regions = Region.query.filter_by(reg_name=reg_name).first()

			if regions:
				flash('Region already exists', category='error')
			elif len(reg_name) < 4:
				flash('Region name must be greater than 4 characters', category='error')
			elif len(reg_description) > 250:
				flash('Region description must be less than 250 characters', category='error')
			elif len(reg_manager) < 4:
				flash('Region manager name must be greater than 4 characters', category='error')
			elif len(reg_manager_phone) < 4:
				flash('Region manager phone number must be greater than 4 characters', category='error')
			elif len(reg_manager_email) < 4:
				flash('Region manager email must be greater than 4 characters', category='error')

			""" Add region to the database """
			new_region = Region(
				reg_name=reg_name,
				reg_description=reg_description,
				reg_image=reg_image,
				reg_manager=reg_manager,
				reg_manager_phone=reg_manager_phone,
				reg_manager_email=reg_manager_email,
				reg_lat=reg_lat,
				reg_lng=reg_lng,
				reg_continent=reg_continent,
				reg_country=reg_country,
				reg_state=reg_state,
				reg_city = reg_city,
				reg_type=reg_type
			)
			db.session.add(new_region)
			db.session.commit()
			flash('Region was added successfully', category='success')
			return redirect(url_for('regions.regions'))
		else:
			flash('Region not found!', category='error')

	return render_template('add_region_form.html', user=current_user, form=form)


# GET CONTINENTS
@bp.route('/regions/get_continents', methods=['GET', 'POST'])
@login_required
def get_continents():
	continents = [
		{
			'name': 'Africa',
			'value': 'Africa',
			'lat': '8.7832',
			'lng': '34.5085'
		},
		{
			'name': 'Asia',
			'value': 'Asia',
			'lat': '34.0479',
			'lng': '100.6197'
		},
		{
			'name': 'Europe',
			'value': 'Europe',
			'lat': '54.5260',
			'lng': '15.2551'
		},
		{
			'name': 'North America',
			'value': 'North America',
			'lat': '70',
			'lng': '105'
		},
		{
			'name': 'South America',
			'value': 'South America',
			'lat': '8.7832',
			'lng': '55.4915'
		},
		{
			'name': 'Oceania',
			'value': 'Oceania',
			'lat': '22.7359',
			'lng': '140.0188'
		}
	]

	return continents


# GETS COUNTRIES BASED ON CONTINENT
@bp.route('/regions/get_countries/<continent>', methods=['POST'])
@login_required
def get_countries(continent):
	locations = [
		{
			'continent': 'Africa',
			'countries': [
				'Algeria',
				'Angola',
				'Benin',
				'Botswana',
				'Burkina Faso',
				'Burundi',
				'Cameroon',
				'Cape Verde',
				'Central African Republic',
				'Chad',
				'Comoros',
				'Djibouti',
				'DR Congo',
				'Egypt',
				'Equatorial Guinea',
				'Eritrea',
				'Eswatini',
				'Ethiopia',
				'Gabon',
				'Gambia',
				'Ghana',
				'Guinea',
				'Guinea Bissau',
				'Ivory Coast',
				'Kenya',
				'Lesotho',
				'Liberia',
				'Libya',
				'Madagascar',
				'Malawi',
				'Mali',
				'Mauritania',
				'Mauritius',
				'Morocco',
				'Mozambique',
				'Namibia',
				'Niger',
				'Nigeria',
				'Republic of the Congo',
				'Rwanda',
				'Sao Tome and Principe',
				'Senegal',
				'Seychelles',
				'Sierra Leone',
				'Somalia',
				'South Africa',
				'South Sudan',
				'Sudan',
				'Tanzania',
				'Togo',
				'Tunisia',
				'Uganda',
				'Zambia',
				'Zimbabwe'
			],
		},
		{
			'continent': 'Asia',
			'countries': [
				'Afghanistan',
				'Armenia',
				'Azerbaijan',
				'Bahrain',
				'Bangladesh',
				'Bhutan',
				'British Indian Ocean',
				'Brunei',
				'Cambodia',
				'China',
				'Cyprus',
				'Egypt',
				'Georgia',
				'Hong Kong',
				'India',
				'Indonesia',
				'Iran',
				'Iraq',
				'Israel',
				'Japan',
				'Jordan',
				'Kazakhstan',
				'Kuwait',
				'Kyrgyzstan',
				'Laos',
				'Lebanon',
				'Macau',
				'Maldives',
				'Mongolia',
				'Myanmar',
				'Nepal',
				'North Korea',
				'Oman',
				'Pakistan',
				'Palestine',
				'Philippines',
				'Qatar',
				'Russia',
				'Saudi Arabia',
				'Singapore',
				'South Korea',
				'Sri Lanka',
				'Syria',
				'Taiwan',
				'Tajikistan',
				'Thailand',
				'Timor-Leste',
				'Turkey',
				'Turkmenistan',
				'United Arab Emirates',
				'Uzbekistan',
				'Vietnam',
				'Yemen'
			]
		},

		{
			'continent': 'Europe',
			'countries': [
				'Albania',
				'Andorra',
				'Armenia',
				'Austria',
				'Azerbaijan',
				'Belarus',
				'Belgium',
				'Bosnia',
				'Bulgaria',
				'Croatia',
				'Cyprus',
				'Czechia',
				'Denmark',
				'Estonia',
				'Finland',
				'France',
				'Georgia',
				'Germany',
				'Greece',
				'Herzegovina',
				'Hungary',
				'Iceland',
				'Ireland',
				'Italy',
				'Kazakhstan',
				'Latvia',
				'Liechtenstein',
				'Lithuania',
				'Luxembourg',
				'Malta',
				'Moldova',
				'Monaco',
				'Montenegro',
				'Netherlands',
				'North Macedonia',
				'Norway',
				'Poland',
				'Portugal',
				'Romania',
				'San Marino',
				'Serbia',
				'Slovakia',
				'Slovenia',
				'Spain',
				'Sweden',
				'Switzerland',
				'Ukraine',
				'United Kingdom'
			]
		},
		{
			'continent': 'North America',
			'countries': [
				'Canada',
				'United States',
				'Mexico'
			]
		},
		{
			'continent': 'South America',
			'countries': [
				'Antigua',
				'Barbuda',
				'Bahamas',
				'Barbados',
				'Belize',
				'Costa Rica',
				'Cuba',
				'Dominica',
				'Dominican Republic',
				'El Salvador',
				'Grenada',
				'Guatemala',
				'Haiti',
				'Honduras',
				'Jamaica',
				'Nicaragua',
				'Panama',
				'Saint Kitts',
				'Saint Lucia',
				'Saint Vincent',
				'Trinidad',
				'Tobago'
			]
		},
		{
			'continent': 'Oceania',
			'countries': [
				'Australia',
				'Fiji Islands',
				'Guam'
				'Kiribati',
				'Marshall Islands',
				'Micronesia',
				'Nauru',
				'New Zealand',
				'Palau',
				'Papua New Guinea',
				"Philippines",
				'Samoa',
				'Solomon Islands',
				'Tonga',
				'Tuvalu',
				'Vanuatu'
			]
		}
	]

	for loc in locations:
		if loc['continent'] == continent:
			return loc['countries']



# GETS CITIES BASED ON STATE
@bp.route('/regions/get_cities/<state_code>', methods=['POST'])
@login_required
def get_cities(state_code):
	# Query DB for cities based on state code
	cities = City.query.filter_by(state_code=state_code).order_by('name').all()

	# create a list of city names
	cities_list= []

	# loop through the cities and append the names to the list
	for city in cities:
		cities_list.append(city.name)

	# return the list of city names as a json object
	return jsonify(cities_list)


#request.referrer