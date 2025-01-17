# config.py
from forms import *
import secrets


class Config:
    SECRET_KEY = secrets.token_hex(16)
    DATABASE = "users.db"
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8080


# config/emissions_config.py

CALCULATOR_CONFIG = {
    "sections": {
        "introduction": {
            "title": "Introduction",
            "text": """
            <h1 class="text-3xl font-bold text-gray-800 mb-4">Energy Consumption across the Digital Value Chain</h1>

            <p class="text-gray-700 mb-4">
                The largest energy consumers are typically data centers and network infrastructure, followed by end-user device consumption. Our calculation model focuses on these three; therefore, categories 1, 5, and 6 are not included.
            </p>

            <div class="text-gray-700">
                <p><strong>Development and Design:</strong> Electricity consumption in offices and development environments.</p>
                <p><strong>Hosting and Data Processing:</strong> High electricity use in data centers (servers, cooling, networks).</p>
                <p><strong>Content Delivery:</strong> Energy for global networks and CDN infrastructure.</p>
                <p><strong>End-User Consumption:</strong> Power used by end-user devices and networking technology.</p>
                <p><strong>Maintenance and Updates:</strong> Electricity for updates and continuous integration.</p>
                <p><strong>Disposal:</strong> Energy for recycling and waste management.</p>
            </div>

            <p class="text-gray-700 mt-4">In addition, no hardware emissions are included in the model.</p>

            """,
            "fields": {},  # No fields in the introduction section
        },
        "product_overview": {
            "title": "Product Overview",
            "fields": {
                "product_name": {
                    "type": "url",
                    "label": "Name of your digital Product",
                    "info": "Enter the URL of your product",
                },
                "product_type": {
                    "type": "select",
                    "label": "Type of digital Product",
                    "info": "Select the type of your product",
                    "options": {
                        "website": {"label": "Website"},
                        "app": {"label": "App"},
                        "podcast": {"label": "Podcast"},
                        "newsletter": {"label": "Newsletter"},
                        "epaper": {"label": "E-Paper"},
                    },
                },
                "country": {
                    "type": "select",
                    "label": "Country",
                    "info": "Select the country of operation",
                    "options": {
                        "usa": {"label": "USA"},
                        "germany": {"label": "Germany"},
                        "france": {"label": "France"},
                        "uk": {"label": "UK"},
                        "poland": {"label": "Poland"},
                        "austria": {"label": "Austria"},
                        "sweden": {"label": "Sweden"},
                        "china": {"label": "China"},
                        "india": {"label": "India"},
                        "canada": {"label": "Canada"},
                        "mexico": {"label": "Mexico"},
                        "brasilia": {"label": "Brasilia"},
                        "south_africa": {"label": "South Africa"},
                    },
                },
            },
        },
        "hosting": {  # Renamed to data_center_emissions for clarity
            "title": "Data Center Emissions",
            "fields": {
                "cloud_provider": {
                    "type": "select",
                    "label": "Cloud Provider",
                    "options": {
                        "aws": {"label": "AWS", "emission_factor": 0.0005},
                        "gcp": {"label": "Google Cloud", "emission_factor": 0.0004},
                        "azure": {"label": "Azure", "emission_factor": 0.00045},
                        "other": {"label": "Other", "emission_factor": 0.0006},
                    },
                },
                "server_hours": {
                    "type": "number",
                    "label": "Server Hours per Month",
                    "emission_factor": 0.0001,
                },
                "server_type": {
                    "type": "select",
                    "label": "Server Type",
                    "options": {
                        "small": {"label": "Small (2 vCPU)", "multiplier": 1},
                        "medium": {"label": "Medium (4 vCPU)", "multiplier": 2},
                        "large": {"label": "Large (8 vCPU)", "multiplier": 4},
                    },
                },
            },
        },
        "traffic": {
            "title": "Traffic",
            "fields": {
                "monthly_users": {
                    "type": "number",
                    "label": "Monthly Active Users",
                    "emission_factor": 0.00001,
                },
                "page_size": {
                    "type": "number",
                    "label": "Average Page Size (KB)",
                    "emission_factor": 0.000002,
                },
                "pages_per_visit": {
                    "type": "number",
                    "label": "Average Pages per Visit",
                    "emission_factor": 0.000005,
                },
            },
        },
        "storage": {
            "title": "Storage",
            "fields": {
                "database_size": {
                    "type": "number",
                    "label": "Database Size (GB)",
                    "emission_factor": 0.0002,
                },
                "storage_size": {
                    "type": "number",
                    "label": "File Storage Size (GB)",
                    "emission_factor": 0.0001,
                },
                "backup_frequency": {
                    "type": "select",
                    "label": "Backup Frequency",
                    "options": {
                        "daily": {"label": "Daily", "multiplier": 30},
                        "weekly": {"label": "Weekly", "multiplier": 4},
                        "monthly": {"label": "Monthly", "multiplier": 1},
                    },
                },
            },
        },
    }
}

# ########### FORM CONFIG ###########
# FORM_CONFIG = {
#     1: {
#         "title": "Introduction",
#         "description": """
# Energy Consumption across the digital Value Chain

# The largest energy consumers are typically data centers and network infrastructure, followed by end-user device consumption. Our calculation model focuses on these three, therefore category 1., 5., and 6. are not included.
# Development and Design: Electricity consumption in offices and development environments.
# Hosting and Data Processing: High electricity use in data centers (servers, cooling, networks).
# Content Delivery: Energy for global networks and CDN infrastructure.
# End-User Consumption: Power used by end-user devices and networking technology.
# Maintenance and Updates: Electricity for updates and continuous integration.
# Disposal: Energy for recycling and waste management.
# In addition no hardware emissions are included in the model.
#         """,
#         "form_class": EmptyForm,
#         "session_key": "basic_info",
#     },
#     2: {
#         "title": "Product Overview",
#         "description": "Enter basic information about your digital product",
#         "form_class": DigitalProductForm,
#         "session_key": "product_info",
#     },
#     3: {
#         "title": "Hosting & Data Processing",
#         "description": "Enter information about product usage and downloads",
#         "form_class": UsageMetricsForm,
#         "session_key": "usage_metrics",
#     },
#     4: {
#         "title": "Content Delivery",
#         "description": "Enter information about advertisements if applicable",
#         "form_class": AdvertisementForm,
#         "session_key": "ad_info",
#     },
#     5: {
#         "title": "End-User Consumption",
#         "description": "Enter information about your data center usage",
#         "form_class": DataCenterForm,
#         "session_key": "datacenter_info",
#     },
# }
