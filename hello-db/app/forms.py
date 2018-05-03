from flask_wtf import FlaskForm
from wtforms import StringField, validators

class HelloForm(FlaskForm):
	name = StringField('Name', [validators.DataRequired()])
	icecream_fav = StringField('Favorite Ice Cream', [validators.DataRequired()])