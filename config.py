# config.py
from forms import *

FORM_CONFIG = {
    1: {
        "title": "Basic Product Information",
        "description": "Enter the basic information about your digital product",
        "form_class": BasicProductInfoForm,
        "session_key": "basic_info",
    },
    2: {
        "title": "Impression Statistics",
        "description": "Enter information about your product's impressions across different devices",
        "form_class": ImpressionStatsForm,
        "session_key": "impression_stats",
    },
    3: {
        "title": "Usage Metrics",
        "description": "Enter information about product usage and downloads",
        "form_class": UsageMetricsForm,
        "session_key": "usage_metrics",
    },
    4: {
        "title": "Advertisement Information",
        "description": "Enter information about advertisements if applicable",
        "form_class": AdvertisementForm,
        "session_key": "ad_info",
    },
    5: {
        "title": "Data Center Information",
        "description": "Enter information about your data center usage",
        "form_class": DataCenterForm,
        "session_key": "datacenter_info",
    },
}
