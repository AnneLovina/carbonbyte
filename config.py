# config.py
import secrets


class Config:
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
                    "info": "e.g. carbonbyte.org or Digtal Podcast",
                },
                "product_type": {
                    "type": "select",
                    "label": "Type of digital Product",
                    "info": "Select the type of your product.",
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
        "analytics": {
            "title": "Analytics",
            "sections": {
                "basic_metrics": {
                    "title": "Basic Product Metrics",
                    "collapsible": True,
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
                    }
                },
                "download_metrics": {
                    "title": "Download Statistics",
                    "collapsible": True,
                    "fields": {
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
                    }
                },
                "device_impressions": {
                    "title": "Device-specific Impressions",
                    "collapsible": True,
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
                    }
                }
            }
        },
        "results": {
            "title": "Review & Submit",
            "text": """
            <h2 class="text-2xl font-bold text-gray-800 mb-4">Please Review Your Inputs</h2>
            
            <p class="text-gray-700 mb-4">
                Before submitting, please carefully review all the values you've entered in the previous sections. 
                Make sure all numbers and selections are accurate, as they directly impact your carbon footprint calculation.
            </p>

            <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-4">
                <p class="text-yellow-700">
                    <strong>Important:</strong> Once you're confident that all entries are correct, 
                    click the submit button below to see your detailed carbon footprint results.
                </p>
            </div>
            """,
            "fields": {},
        },
    }
}



LEGAL_CONFIG =  {
    "imprint": """Anne Dyck
    Mainzer Straße 5,10247 Berlin, Mail.""",
    "privacy": "Your company's privacy policy goes here.",
}

LANDING_PAGE_CONFIG = {
    "hero": {
        "title": "Track Your Digital Carbon Footprint",
        "description": "Did you know that every digital product, from websites to mobile apps, contributes to your business's carbon footprint? The energy used by your infrastructure, the data transferred, and the devices accessing your digital products all result in emissions. With our calculator, businesses can measure the carbon impact of their digital products, understand where emissions are generated, and take meaningful steps towards reducing their environmental footprint.",
        "cta_text": "Ready to take action?"
    },
    "features": [
        {
            "title": "Hosting & Data Processing",
            "description": "Calculate the carbon footprint of your hosting environment and data centers,",
            "bg_class": "bg-[#F3E5D7]"
        },
        {
            "title": "Content Delivery",
            "description": "Analyze emissions from global network infrastructure and content delivery networks.",
            "bg_class": "bg-[#E7D8C9]"
        },
        {
            "title": "End-User Consumption",
            "description": "Track emissions from various end-user devices and network connections.",
            "bg_class": "bg-[#D8C3A5]"
        }
    ],
    "value_chain": {
        "title": "Want to know more about the value chain of a digital product?",
        "description": """The value chain consists of several stages where electricity is consumed. The largest energy consumers are typically data centers and network infrastructure, followed by end-user device consumption.Most companies focus on the emissions from data centers (which is required by the GHG protocol), however it can be interesting to have a look at the whole value chain.This calculation model focuses on the categories 3., 4., and 5. (marked in bold), therefore it does not show a whole Product carbon footprint (PCF). If you need to support to calculate the whole PCF please contact us.""",
        "sections": [
            {
                "title": "Development and Design",
                "description": """In this phase, the digital product is designed and programmed.
                electricity_consumption: [
                    Hardware such as computers, laptops, and development servers.,
                    Software tools and development environments.",
                    Collaboration platforms (e.g., cloud services for project management).,
                    Office infrastructure (lighting, heating, and cooling).
                ]""",
            },
            {
                "title": "Hosting and Data Processing",
                "description": "Here, the digital product is hosted in a data center.",
                "electricity_consumption": [
                    "Server hardware for processing requests and storing data.",
                    "Cooling systems (e.g., air conditioning or water cooling) for server rooms.",
                    "Network devices like routers, switches, and load balancers.",
                    "Backup power supplies (UPS, generators).",
                    "Redundant server infrastructure for fail-safety."
                ]
            },
            {
                "title": "Content Delivery",
                "description": "To deliver data and services quickly to the end user, Content Delivery Networks (CDNs) and decentralized servers are used.",
                "electricity_consumption": [
                    "Global network infrastructure for data transfer.",
                    "CDN servers for caching content in various regions.",
                    "Data compression and optimization, which require additional computing power."
                ]
            },
            {
                "title": "End-User Consumption",
                "description": "End-users access the digital product via various devices.",
                "electricity_consumption": [
                    "Smartphones, tablets, laptops, and desktop PCs.",
                    "Internet routers and modems for connecting to the internet.",
                    "Mobile networks (4G, 5G) and Wi-Fi infrastructure.",
                    "Display technologies (e.g., OLED, LCD) for viewing content."
                ]
            },
            {
                "title": "Maintenance and Updates",
                "description": "Regular updates and improvements are necessary.",
                "electricity_consumption": [
                    "Server load for software updates and patches.",
                    "Data transfer for updates to end-user devices.",
                    "Development infrastructure for continuous integration and deployment (CI/CD)."
                ]
            },
            {
                "title": "Disposal and Recycling",
                "description": "At the end of the product’s lifecycle, devices need to be disposed of or recycled.",
                "electricity_consumption": [
                    "Recycling processes for old hardware.",
                    "Transport and processing of electronic waste.",
                    "Energy consumption for recovering raw materials (e.g., metals)."
                ]
            }
        ]
    },
    "faq": [
        {
            "question": "What does this tool do?",
            "answer": "Our tool helps companies calculate the CO₂ emissions of their digital products. It considers emissions generated by server infrastructure, data transmission, and usage on end-user devices."
        },
        {
            "question": "Why should I calculate the emissions of my digital products?",
            "answer": "While not currently required by GHG Protocol and CSRD, knowing these emissions helps you:",
            "list": [
                "Gain transparency about your carbon footprint",
                "Take proactive sustainability measures",
                "Prepare for potential regulatory changes"
            ]
        },
        {
            "question": "What data do I need?",
            "answer": "The required data is directly requested within the tool, guiding you step-by-step through the process. Our Methodology section provides tips on sourcing the necessary data."
        },
        {
            "question": "How accurate are the calculations?",
            "answer": "Our calculations are based on scientifically validated models and the latest available data. Accuracy depends on the quality of your input data, but results provide a reliable foundation for sustainability planning."
        },
        {
            "question": "Will my data be stored?",
            "answer": "No, your data is processed anonymously and not stored permanently. Data protection and privacy are our top priorities."
        },
        {
            "question": "Can I identify specific reduction potentials with the tool?",
            "answer": "The tool focuses on creating transparency, showing you where emissions occur and in what magnitude. Reduction measures in digital products are often complex.\nPotential levers for emission reduction include:\n- Using data centers powered by renewable energy.\n- Optimizing hosting and server utilization, e.g., through dynamic scaling.\n- Reducing data volumes through software optimization.\n- Employing caching or Content Delivery Networks (CDNs) to minimize data transmission.\nThe tool lays the foundation to evaluate such potentials effectively."
        },
        {
            "question": "Something is missing in the calculation?",
            "answer": "Ad social media, Own data center calculation, diffrent Ansatz for Data Center – contact us"
        },
        {
            "question": "How does your tool differ from others on the market?",
            "answer": "Our tool is specifically designed for digital products. It offers an intuitive interface, reliable results, and a transparent methodology. Additionally, it goes beyond simple calculations by helping you interpret results and develop strategic actions."
        },
        {
            "question": "What does it cost to use the tool?",
            "answer": "The tool is initially available for free. In the future, advanced features or more detailed analyses might come with a fee, but the basic version will remain free."
        },
        {
            "question": "Where can I learn more about the tool's methodology?",
            "answer": "We prioritize transparency. In the Methodology section, you'll find a detailed explanation of all formulas, calculations, and data sources used. This ensures you understand how the results are derived and the scientific principles behind them.\nYou can find our whole methodology here: link git hub"
        }
    ],
    "legal": LEGAL_CONFIG
}

