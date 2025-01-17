from parameters import Parameter as P
from datetime import datetime


def calculate(inputs):
    result = {**inputs}
    result["result_data_center"] = -1
    result["result_advertising"] = -1
    result["result_fixed_line"] = -1
    result["result_cellular_line"] = -1
    result["result_cdn"] = -1

    emission_factor = P.COUNTRY_CARBON_INTENSITY.get(
        inputs["country"], P.COUNTRY_CARBON_INTENSITY_DEFAULT
    )

    reporting_period_days = (
        datetime.strptime(inputs["end_date"], "%Y-%m-%d")
        - datetime.strptime(inputs["start_date"], "%Y-%m-%d")
    ).days

    return result


# {
#     "ad_emission_factor": "50",
#     "ad_impressions": "1000000",
#     "computer_impressions": "100000",
#     "country": "germany",
#     "data_center_co2_emissions": "99212",
#     "data_center_energy": "1222212",
#     "data_center_total_spend": "11111",
#     "data_size": "2000",
#     "download_service_time": "222414",
#     "download_size": "13231",
#     "end_date": "2024-12-31",
#     "ereader_impressions": "0",
#     "number_of_downloads": "432",
#     "product_name": "idealo.de",
#     "product_size": "1000",
#     "product_type": "website",
#     "smartphone_impressions": "50000",
#     "start_date": "2024-01-01",
#     "tablet_impressions": "10000",
#     "time_on_product": "200000",
#     "tv_impressions": "100",
#     "video_viewing_time": "123333",
# }
