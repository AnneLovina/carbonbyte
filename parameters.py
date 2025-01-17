class Parameter:
    DATA_CENTER_EMISSION_INTENSITY_GREEN = 0.040  # [kg CO2e/Euro] (Google, Microsoft)
    DATA_CENTER_EMISSION_INTENSITY_MIXED = 0.080  # [kg CO2e/Euro] (AWS)
    DATA_CENTER_EMISSION_INTENSITY_CONSERVATIVE = 0.180  # [kg CO2e/Euro]

    DATA_CENTER_SERVER_POWER_CONSUMPTION = 200  # [watt]
    DATA_CENTER_STORAGE_POWER_CONSUMPTION = 500  # [watt]
    DATA_CENTER_NETWORK_POWER_CONSUMPTION = 100  # [watt]
    DATA_CENTER_COOLING_AND_OTHER_TECH = 30  # [%]
    AD_EMISSION_FACTOR = 70.000  # [gCO2 per 1000 AI]
    FIXED_LINE_ENERGY_INTENSITY_2024 = (
        0.015  # [kwh/GB] (Halved every 2 years from 0.06 in 2020)
    )
    MOBILE_LINE_ENERGY_INTENSITY = 0.140  # [kwh/GB]
    MEAN_CARBON_INTENSITY_CDN_ELECTRICITY = 0.212  # [kg/kWh]
    MEAN_TOTAL_DATA_VOLUME_PER_HOUSEHOLD = 453  # [GB]
    USER_HOUSEHOLD_MODEM_ROUTER_POWER = 10  # [w]
    MEAN_ELECTRICAL_ENERGY_USED_BY_CPE_PER_GB = 0.02  # [kwh/GB]
    LAPTOP_SHARE = 0.70  # [%]
    DESKTOP_SHARE = 0.30  # [%]

    # Country-specific emission factors
    COUNTRY_CARBON_INTENSITY = {
        "USA": 0.05790,  # [kg/kwh]
        "GERMANY": 0.05980,  # [kg/kwh]
        "FRANCE": 0.01580,  # [kg/kwh]
        "UK": 0.03150,  # [kg/kwh]
        "POLAND": 0.11750,  # [kg/kwh]
        "AUSTRIA": 0.01970,  # [kg/kwh]
        "SWEDEN": 0.00830,  # [kg/kwh]
        "CHINA": 0.08580,  # [kg/kwh]
        "INDIA": 0.11250,  # [kg/kwh]
        "CANADA": 0.01900,  # [kg/kwh]
        "MEXICO": 0.07760,  # [kg/kwh]
        "BRASILIA": 0.01560,  # [kg/kwh]
        "AUSTRALIA": 0.09450,  # [kg/kwh]
        "JAPAN": 0.07600,  # [kg/kwh]
        "HUNGARY": 0.03730,  # [kg/kwh]
        "SOUTH_AFRICA": 0.13810,  # [kg/kwh]
        "SPAIN": 0.03050,  # [kg/kwh]
        "IRELAND": 0.04820,  # [kg/kwh]
        "SLOVAKIA": 0.02770,  # [kg/kwh]
        "BELGIUM": 0.02330,  # [kg/kwh]
    }
    COUNTRY_CARBON_INTENSITY_DEFAULT = COUNTRY_CARBON_INTENSITY["USA"]
