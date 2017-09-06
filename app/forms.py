from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired


class LoginForm(Form):

    
    
    summoner1 = StringField('Name 1', validators=[DataRequired()])
    summoner2 = StringField('Name 2', validators=[DataRequired()])   

    REGION_ABBREV = ('NA', 'EUW', 'EUNE', 'KR', 'RUS', 'BR', 'OCE', 'JP', 'TR', 'LAN', 'LAS')
    
    region = SelectField(label='Region', 
    choices=[(region, region) for region in REGION_ABBREV])

