# config.py
from forms import *
import secrets


class Config:
    SECRET_KEY = secrets.token_hex(16)
    DATABASE = "users.db"
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8080


########### FORM CONFIG ###########
FORM_CONFIG = {
    1: {
        "title": "Introduction",
        "description": """
Energy Consumption across the digital Value Chain

The largest energy consumers are typically data centers and network infrastructure, followed by end-user device consumption. Our calculation model focuses on these three, therefore category 1., 5., and 6. are not included. 
Development and Design: Electricity consumption in offices and development environments.
Hosting and Data Processing: High electricity use in data centers (servers, cooling, networks).
Content Delivery: Energy for global networks and CDN infrastructure.
End-User Consumption: Power used by end-user devices and networking technology.
Maintenance and Updates: Electricity for updates and continuous integration.
Disposal: Energy for recycling and waste management.
In addition no hardware emissions are included in the model. 
        """,
        "form_class": EmptyForm,
        "session_key": "basic_info",
    },
    2: {
        "title": "Product Overview",
        "description": "Enter basic information about your digital product",
        "form_class": DigitalProductForm,
        "session_key": "product_info",
    },
    3: {
        "title": "Hosting & Data Processing",
        "description": "Enter information about product usage and downloads",
        "form_class": UsageMetricsForm,
        "session_key": "usage_metrics",
    },
    4: {
        "title": "Content Delivery",
        "description": "Enter information about advertisements if applicable",
        "form_class": AdvertisementForm,
        "session_key": "ad_info",
    },
    5: {
        "title": "End-User Consumption",
        "description": "Enter information about your data center usage",
        "form_class": DataCenterForm,
        "session_key": "datacenter_info",
    },
}
