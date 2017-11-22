#!flask/bin/python
from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired


class LoginForm(Form):

    
    
    summoner1 = StringField('Name 1', validators=[DataRequired()])
    summoner2 = StringField('Name 2', validators=[DataRequired()])   

    REGION_ABBREV = ('NA', 'EUW', 'EUNE', 'KR', 'RUS', 'BR', 'OCE', 'JP', 'TR', 'LAN', 'LAS')

    QUEUETYPE_ABBREV = ('Solo/Duo', 'Flex')

    SEASON_ABBREV = ('Season 7 (2017)', 'Preseason 8', 'Season 8 (2018)') 
    
    region = SelectField(label='Region', 
    choices=[(region, region) for region in REGION_ABBREV])

    queuetype = SelectField(label='Queue Type', 
    choices=[(queuetype, queuetype) for queuetype in QUEUETYPE_ABBREV])

    season = SelectField(label='Season', 
    choices=[(season, season) for season in SEASON_ABBREV])
