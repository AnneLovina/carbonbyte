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

          <p class="text-gray-700 mb-4">
              CarbonByte is a web application designed to help users estimate the carbon footprint of their digital products, such as websites, apps, podcasts, newsletters, or e-papers. Users can input various metrics related to their product's lifecycle, including data center usage, advertising, and end-user interaction. The model estimates CO2 emissions by focusing on the primary energy consumers in the digital value chain:

          <div class="text-gray-700">
              <p><strong>1. Data Center Emissions:</strong> Electricity use in data centers (servers, cooling, networks).</p>
              <p><strong>2. Advertising Emissions:</strong> Calculated using the number of ad impressions and an emission factor (either user-provided or a default value from here: https://github.com/AnneLovina/carbonbyte/blob/main/parameters.py)</p>
              <p><strong>3. Content Delivery (Network) Emissions:</strong> Estimated based on the total data transferred (calculated from product size, video viewing time, and downloads) across fixed and mobile networks. It uses energy intensity factors (kWh/GB) for each network type and applies a country-specific carbon intensity factor (kg CO2e/kWh) for electricity.</p>
              <p><strong>4. End-User Device Emissions:</strong> Calculated based on the time users spend on the product, distributed across different device types (laptops, desktops, smartphones, tablets, TVs, e-readers) according to impression counts. It considers the average power consumption of each device type and the carbon intensity of electricity in the specified country.</p>
          </div>

          <p class="text-gray-700 mt-4">It does not currently include emissions related to:
Development and Design phases.
Maintenance and Updates (e.g., CI/CD pipelines).
Hardware manufacturing (embodied carbon).
Product disposal and recycling.
Constants and Emission Factors: Default values for energy intensity, device power consumption, data transfer bitrates, and country carbon intensity are defined here: https://github.com/AnneLovina/carbonbyte/blob/main/parameters.py</p>
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



LEGAL_CONFIG = {
    "imprint": """
        <h2>Imprint</h2>
        <p><strong>Anne Dyck</strong><br>
        Straße x<br>
        102xx Berlin<br>
        Germany</p>
        
        <strong>Email:</strong> contact@carbonbyte.org</p>
        
        <h3>Liability for Content</h3>
        <p>As a service provider, we are responsible for our own content on these pages in accordance with general legislation, pursuant to § 7 (1) TMG. However, under §§ 8 to 10 TMG, we are not obliged to monitor transmitted or stored third-party information or to investigate circumstances indicating illegal activity. Obligations to remove or block the use of information in accordance with general laws remain unaffected. Liability in this regard is only possible from the point in time at which a specific legal infringement becomes known. Upon notification of such violations, we will remove this content immediately.</p>
        
        <h3>Liability for Links</h3>
        <p>Our website contains links to external third-party websites over which we have no control. Therefore, we cannot assume any liability for these external contents. The respective provider or operator of the linked pages is always responsible for their content. The linked pages were checked for possible legal violations at the time of linking. No unlawful content was identifiable at that time. A permanent content check of the linked pages is, however, not reasonable without concrete evidence of a legal violation. Upon becoming aware of any such infringements, we will remove the respective links immediately.</p>
        
        <h3>Copyright</h3>
        <p>The content and works created by the site operators on these pages are subject to German copyright law. Duplication, processing, distribution, or any form of commercialization beyond the scope of copyright law shall require the prior written consent of the respective author or creator. Downloads and copies of this site are only permitted for private, non-commercial use. Insofar as the content on this site was not created by the operator, the copyrights of third parties are respected. In particular, third-party content is identified as such. Should you nevertheless become aware of a copyright infringement, please inform us accordingly. Upon becoming aware of any violations, we will remove such content immediately.</p>
    """,
    "privacy": """
        <h2>Privacy Policy</h2>
        <p>We take the protection of your personal data very seriously. We treat your personal data confidentially and in accordance with statutory data protection regulations and this privacy policy.</p>
        
        <h3>Data Collection</h3>
        <p>We only collect personal data if it is necessary for providing our services. This may include information such as your name, email address, or IP address.</p>
        
        <h3>Usage of Data</h3>
        <p>Collected data is used exclusively to provide, improve, and secure our services. Your data will not be passed on to third parties without your explicit consent, unless legally required.</p>
        
        <h3>Cookies</h3>
        <p>Our website may use cookies to improve the user experience. You can configure your browser to notify you when cookies are being set or to block cookies entirely.</p>
        
        <h3>Your Rights</h3>
        <p>You have the right to request information about the personal data we store about you, to have incorrect data corrected, and to request deletion or restricted processing of your data. You also have the right to object to the processing of your data and to data portability.</p>
        
        <h3>Contact</h3>
        <p>For questions regarding this privacy policy or your personal data, you can contact us at:<br>
        Email: contact@carbonbyte.org</p>
        
        <h3>Changes</h3>
        <p>We reserve the right to modify this privacy policy at any time in accordance with legal requirements.</p>
    """
}


LANDING_PAGE_CONFIG = {
    "hero": {
        "title": "Track Your Digital Carbon Footprint",
        "description": "Did you know that every digital product, from websites to mobile apps, contributes to your business's carbon footprint? The energy used by your infrastructure, the data transferred, and the devices accessing your digital products all result in emissions. With our calculator, businesses can measure the carbon impact of their digital products, understand where emissions are generated, and take meaningful steps towards reducing their environmental footprint.",
        "cta_text": "Ready to take action?"
    },
    "features": [
    {
        "title": "Design & Development",
        "description": "Upstream emissions from software development and design.",
        "status": "not_included",
        "bg_color": "#f5f5f5"
    },
    {
        "title": "Data Center",
        "description": "Server infrastructure and cloud operations.",
        "status": "included",
        "bg_color": "#fff4f2"
    },
    {
        "title": "Advertising",
        "description": "Emissions from ad loading and targeting.",
        "status": "included",
        "bg_color": "#f1fafa"
    },
    {
        "title": "Content Delivery",
        "description": "Streaming and CDN infrastructure.",
        "status": "included",
        "bg_color": "#fffde7"
    },
    {
        "title": "End User",
        "description": "Energy usage of end-user devices.",
        "status": "included",
        "bg_color": "#f5f3f2"
    },
    {
        "title": "Disposal",
        "description": "End-of-life and e-waste emissions.",
        "status": "not_included",
        "bg_color": "#f5f5f5"
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
        "category": "General",
        "questions": [
            {
                "question": "What does the CarbonByte tool do?",
                "answer": "This tool helps companies calculate the CO₂ emissions of their digital products. It considers emissions generated by server infrastructure, data transmission, and usage on end-user devices."
            },
            {
                "question": "Why should I calculate the emissions of my digital products?",
                "answer": "Understanding these emissions helps you:",
                "list": [
                    "Gain transparency about your carbon footprint",
                    "Take proactive sustainability measures",
                    "Prepare for potential regulatory changes"
                ]
            },
            {
                "question": "What does it cost to use the tool?",
                "answer": "The tool is initially available for free."
            }
        ]
    },
    {
        "category": "Data & Methodology",
        "questions": [
            {
                "question": "What data do I need?",
                "answer": "The required data is directly requested within the tool, guiding you step-by-step through the process. The tool also provides tips on sourcing the necessary data."
            },
            {
                "question": "How accurate are the calculations?",
                "answer": "Our calculations are based on scientifically validated models and the available parameter data. Accuracy depends on the quality of your input data, but results provide a reliable foundation for sustainability planning. Please note: We do not assume liability for the accuracy of the results. For further details and assumptions, please refer to our Methodology."
            },
            {
                "question": "Will my data be stored?",
                "answer": "No, your data is processed anonymously and not stored permanently."
            },
            {
                "question": "Where can I learn more about the tool's methodology?",
                "answer": "We prioritize transparency. All formulas, calculations, and data sources are documented in our open source methodology: https://github.com/AnneLovina/carbonbyte."
            }
        ]
    },
    {
        "category": "Emissions Reduction",
        "questions": [
            {
                "question": "Can I identify specific reduction potentials with the tool?",
                "answer": "No. The tool does not automatically suggest reduction potentials. Instead, it provides transparency by showing where emissions occur and in what magnitude."
            }
        ]
    },
    {
        "category": "Feedback & Limitations",
        "questions": [
            {
                "question": "Something is missing in the calculation?",
                "answer": "If your use case includes social media traffic, own data centers, or alternative infrastructure models, please contact us—we’re actively working to expand coverage."
            },
            {
                "question": "How does your tool differ from others on the market?",
                "answer": "Our tool is specifically designed for digital products. It offers an intuitive interface, reliable results, and transparent methodology—plus guidance for action, not just data."
            }
        ]
    }
],

    "legal": LEGAL_CONFIG
}

