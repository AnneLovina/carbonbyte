# config.py
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
            "fields": {},
        },
        "product_overview": {
            "title": "Product Overview",
            "fields": {
                "product_name": {
                    "type": "url",
                    "label": "Name of your digital Product",
                    "info": "e.g. yourfootprint.de or Digtal Podcast",
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
                "start_date": {
                    "type": "date",
                    "label": "Start Date",
                    "info": "Start date of the calculation period",
                },
                "end_date": {
                    "type": "date",
                    "label": "End Date",
                    "info": "End date of the calculation period",
                },
            },
        },
        "user_impressions": {
            "title": "User Impressions",
            "fields": {
                "computer_impressions": {
                    "type": "number",
                    "label": "Computer Impressions",
                    "info": "Impressions on desktop/laptop computers",
                },
                "smartphone_impressions": {
                    "type": "number",
                    "label": "Smartphone Impressions",
                    "info": "Impressions on smartphones",
                },
                "tablet_impressions": {
                    "type": "number",
                    "label": "Tablet Impressions",
                    "info": "Impressions on tablets",
                },
                "tv_impressions": {
                    "type": "number",
                    "label": "TV Impressions",
                    "info": "Impressions on TVs",
                },
                "ereader_impressions": {
                    "type": "number",
                    "label": "E-Reader Impressions",
                    "info": "Impressions on E-Readers",
                },
            },
        },
        "product_usage": {
            "title": "Product Usage",
            "fields": {
                "product_size": {
                    "type": "number",
                    "label": "Size of Product (KB)",
                    "info": "Size of the product in kilobytes",
                },
                "time_on_product": {
                    "type": "number",
                    "label": "Time on Product (Hours)",
                    "info": "Total time spent on the product in hours",
                },
                "video_viewing_time": {
                    "type": "number",
                    "label": "Video Viewing Time (Hours)",
                    "info": "Total video viewing time in hours",
                },
                "number_of_downloads": {
                    "type": "number",
                    "label": "Number of Downloads",
                    "info": "Total number of downloads",
                },
                "download_size": {
                    "type": "number",
                    "label": "Download Size (KB)",
                    "info": "Average size of each download in kilobytes",
                },
                "download_service_time": {
                    "type": "number",
                    "label": "Download Service Time (Hours)",
                    "info": "Time used for download services in hours",
                },
            },
        },
        "advertising": {
            "title": "Advertising",
            "fields": {
                "ad_impressions": {
                    "type": "number",
                    "label": "Ad Impressions",
                    "info": "Number of ad impressions",
                },
                "ad_emission_factor": {
                    "type": "number",
                    "label": "Ad Emission Factor (gCO2e per 1000 AI)",
                    "info": "Emission factor for advertising",
                },
            },
        },
        "data_center": {
            "title": "Data Center",
            "fields": {
                "data_center_co2_emissions": {
                    "type": "number",
                    "label": "Data Center CO2 Emissions (kg CO2)",
                    "info": "CO2 emissions from the data center",
                },
                "data_center_energy": {
                    "type": "number",
                    "label": "Data Center Energy Consumption (kWh)",
                    "info": "Energy consumption of the data center",
                },
                "data_size": {
                    "type": "number",
                    "label": "Data Size (KB)",
                    "info": "Total data size in kilobytes",
                },
                "data_center_total_spend": {
                    "type": "number",
                    "label": "Data Center Total Spend (Euro)",
                    "info": "Total spending on data center services",
                },
            },
        },
    }
}
