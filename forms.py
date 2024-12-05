from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    IntegerField,
    FloatField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import DataRequired, Optional, NumberRange


class BasicProductInfoForm(FlaskForm):
    """Form for mandatory basic product information (In_1 to In_5)"""

    product_name = StringField(
        "Name of digital product",
        validators=[DataRequired()],
        description="Enter the name of your digital product (e.g. yourfootprint.de or Digital Podcast)",
    )

    product_type = SelectField(
        "Product Type",
        choices=[("website", "Website"), ("app", "App"), ("other", "Other")],
        validators=[DataRequired()],
        description="Enter the type of your product",
    )

    country = SelectField(
        "Country",
        # You would want to populate this with a full country list
        choices=[("germany", "Germany"), ("france", "France"), ("other", "Other")],
        validators=[DataRequired()],
        description="In which country or region is your product mostly being used?",
    )

    start_date = DateField(
        "Start date",
        validators=[DataRequired()],
        description="Enter the start date you are reporting for",
    )

    end_date = DateField(
        "End date",
        validators=[DataRequired()],
        description="Enter the end date you are reporting for",
    )

    submit = SubmitField("Next Section")


class ImpressionStatsForm(FlaskForm):
    """Form for impression statistics (In_7 to In_15)"""

    computer_impressions = IntegerField(
        "Computer impressions",
        validators=[Optional()],
        description="Total computer impressions",
    )

    laptop_impressions = IntegerField("Laptop Impressions", validators=[Optional()])

    desktop_impressions = IntegerField("Desktop Impressions", validators=[Optional()])

    smartphone_total = IntegerField("Smartphone total", validators=[Optional()])

    smartphone_ios = IntegerField("Smartphone Impressions IOS", validators=[Optional()])

    smartphone_android = IntegerField(
        "Smartphone Impressions Android", validators=[Optional()]
    )

    tablet_impressions = IntegerField("Tablet Impressions", validators=[Optional()])

    tv_impressions = IntegerField("TV Impressions", validators=[Optional()])

    ereader_impressions = IntegerField("E-Reader impressions", validators=[Optional()])

    submit = SubmitField("Next Section")


class UsageMetricsForm(FlaskForm):
    """Form for usage metrics (In_16 to In_21)"""

    product_size = FloatField(
        "Size of product",
        validators=[DataRequired()],
        description="Size of your digital product",
    )

    product_size_unit = SelectField(
        "Size Unit",
        choices=[("kb", "kByte"), ("mb", "MByte"), ("gb", "GByte")],
        validators=[DataRequired()],
    )

    time_on_product = FloatField(
        "Time on product",
        validators=[DataRequired()],
        description="Total time spent on product",
    )

    time_unit = SelectField(
        "Time Unit",
        choices=[("hr", "Hours"), ("min", "Minutes")],
        validators=[DataRequired()],
    )

    video_viewing_time = FloatField(
        "Video viewing time (hours)", validators=[Optional()]
    )

    downloads_count = IntegerField("Number of Downloads", validators=[Optional()])

    download_size = FloatField("Size of Download", validators=[Optional()])

    download_size_unit = SelectField(
        "Download Size Unit",
        choices=[("kb", "kByte"), ("mb", "MByte")],
        validators=[Optional()],
    )

    download_service_time = FloatField(
        "Download service time (hours)", validators=[Optional()]
    )

    submit = SubmitField("Next Section")


class AdvertisementForm(FlaskForm):
    """Form for advertisement related inputs (In_22 to In_23)"""

    ad_impressions = IntegerField(
        "Ad Impressions",
        validators=[Optional()],
        description="Number of advertisement impressions",
    )

    has_ad_emission_factor = BooleanField("Do you know your ad emission factor?")

    ad_emission_factor = FloatField("Ad Emission Factor", validators=[Optional()])

    ad_emission_unit = SelectField(
        "Emission Factor Unit",
        choices=[("g", "g CO2e per 1000 AI"), ("kg", "kg CO2e per 1000 AI")],
        validators=[Optional()],
    )

    submit = SubmitField("Next Section")


class DataCenterForm(FlaskForm):
    """Form for data center related inputs (In_24 to In_27)"""

    has_dc_emissions = BooleanField(
        "Do you have information on the emissions from your data center?"
    )

    dc_emissions = FloatField("Data Center CO2 Emissions", validators=[Optional()])

    dc_emissions_unit = SelectField(
        "Emissions Unit",
        choices=[("kg", "kg CO2"), ("t", "t CO2")],
        validators=[Optional()],
    )

    dc_energy = FloatField("Data Center energy (kWh)", validators=[Optional()])

    dc_data_size = FloatField("Data size", validators=[Optional()])

    dc_data_unit = SelectField(
        "Data Size Unit",
        choices=[("kb", "kByte"), ("mb", "MByte"), ("gb", "GByte")],
        validators=[Optional()],
    )

    dc_spend = FloatField("Data center total spend", validators=[Optional()])

    dc_spend_currency = SelectField(
        "Currency",
        choices=[("eur", "Euro"), ("usd", "Dollar")],
        validators=[Optional()],
    )

    submit = SubmitField("Complete")
