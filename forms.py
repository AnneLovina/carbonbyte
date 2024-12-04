# forms.py
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ServerInfrastructureForm(FlaskForm):
    server_location = SelectField('Server Location', 
        choices=[
            ('europe', 'Europe (0.23 kg CO2/kWh)'),
            ('north_america', 'North America (0.38 kg CO2/kWh)'),
            ('asia', 'Asia (0.54 kg CO2/kWh)')
        ],
        validators=[DataRequired()]
    )
    server_type = SelectField('Server Type',
        choices=[
            ('shared', 'Shared Hosting (Lower impact)'),
            ('dedicated', 'Dedicated Server (Medium impact)'),
            ('cloud', 'Cloud Server (Variable impact)')
        ],
        validators=[DataRequired()]
    )
    cpu_usage = IntegerField('Average Monthly CPU Usage (%)',
        validators=[
            DataRequired(),
            NumberRange(min=0, max=100)
        ]
    )
    submit = SubmitField('Next Section')

class StorageForm(FlaskForm):
    storage_type = SelectField('Storage Type',
        choices=[
            ('ssd', 'SSD Storage'),
            ('hdd', 'HDD Storage'),
            ('hybrid', 'Hybrid Storage')
        ],
        validators=[DataRequired()]
    )
    storage_amount = IntegerField('Storage Amount (GB)',
        validators=[
            DataRequired(),
            NumberRange(min=1)
        ]
    )
    submit = SubmitField('Next Section')

class NetworkingForm(FlaskForm):
    monthly_bandwidth = IntegerField('Monthly Bandwidth Usage (GB)',
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )
    cdn_usage = SelectField('CDN Usage',
        choices=[
            ('none', 'No CDN'),
            ('partial', 'Partial CDN Integration'),
            ('full', 'Full CDN Integration')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Next Section')

# Additional forms for other sections...