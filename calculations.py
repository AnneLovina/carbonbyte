from parameters import Parameter as P
from datetime import datetime


def calculate(inputs):
    inputs = {**inputs}

    inputs["data_center_co2_emissions"] = float(inputs["data_center_co2_emissions"])
    inputs["ad_impressions"] = float(inputs["ad_impressions"])
    inputs["ad_emission_factor"] = float(inputs["ad_emission_factor"])
    inputs["product_size"] = float(inputs["product_size"])
    inputs["time_on_product"] = float(inputs["time_on_product"])
    inputs["video_viewing_time"] = float(inputs["video_viewing_time"])
    inputs["number_of_downloads"] = float(inputs["number_of_downloads"])
    inputs["download_size"] = float(inputs["download_size"])
    inputs["download_service_time"] = float(inputs["download_service_time"])
    inputs["computer_impressions"] = float(inputs["computer_impressions"])
    inputs["smartphone_impressions"] = float(inputs["smartphone_impressions"])
    inputs["tablet_impressions"] = float(inputs["tablet_impressions"])
    inputs["tv_impressions"] = float(inputs["tv_impressions"])
    inputs["ereader_impressions"] = float(inputs["ereader_impressions"])

    result = {}

    emission_factor = P.COUNTRY_CARBON_INTENSITY.get(inputs["country"].upper())

    # Data Center
    result["result_data_center"] = inputs["data_center_co2_emissions"]

    if inputs["ad_emission_factor"] is not None or inputs["ad_emission_factor"] <= 0:
        result["result_advertising"] = (
            inputs["ad_impressions"] * inputs["ad_emission_factor"] / 1000000
        )
    else:
        result["result_advertising"] = inputs["ad_impressions"] * P.AD_EMISSION_FACTOR

    # Impressions
    laptop_impressions = inputs["computer_impressions"] * P.LAPTOP_SHARE
    desktop_impressions = inputs["computer_impressions"] * P.DESKTOP_SHARE

    total_impressions = (
        inputs["computer_impressions"]
        + inputs["smartphone_impressions"]
        + inputs["tablet_impressions"]
        + inputs["tv_impressions"]
        + inputs["ereader_impressions"]
    )
    avg_time_on_product = inputs["time_on_product"] / total_impressions

    result["end_user_devices"] = {
        "laptop_energy": avg_time_on_product
        * laptop_impressions
        * P.LAPTOP_DEVICE_ON_POWER,
        "laptop_emissions": (avg_time_on_product * laptop_impressions)
        * emission_factor,
        "desktop_energy": avg_time_on_product
        * desktop_impressions
        * P.DESKTOP_DEVICE_ON_POWER,
        "desktop_emissions": (avg_time_on_product * desktop_impressions)
        * emission_factor,
        "smartphone_energy": avg_time_on_product
        * inputs["smartphone_impressions"]
        * P.SMARTPHONE_DEVICE_ON_POWER,
        "smartphone_emissions": (avg_time_on_product * inputs["smartphone_impressions"])
        * emission_factor,
        "tablet_energy": avg_time_on_product
        * inputs["tablet_impressions"]
        * P.TABLET_DEVICE_ON_POWER,
        "tablet_emissions": (avg_time_on_product * inputs["tablet_impressions"])
        * emission_factor,
        "tv_energy": avg_time_on_product
        * inputs["tv_impressions"]
        * P.TV_DEVICE_ON_POWER,
        "tv_emissions": (avg_time_on_product * inputs["tv_impressions"])
        * emission_factor,
        "ereader_energy": avg_time_on_product
        * inputs["ereader_impressions"]
        * P.EREADER_DEVICE_ON_POWER,
        "ereader_emissions": (avg_time_on_product * inputs["ereader_impressions"])
        * emission_factor,
    }

    laptop_fixed_line_data_transfer_gb = (
        laptop_impressions * inputs["product_size"]
        + inputs["video_viewing_time"] * P.MEAN_BITRATE_OF_VIDEO_LAPTOP
        # + inputs["download_size"] * inputs["number_of_downloads"] TODO
    ) / (1024 * 1024)

    desktop_fixed_line_data_transfer_gb = (
        desktop_impressions * inputs["product_size"]
        + inputs["video_viewing_time"] * P.MEAN_BITRATE_OF_VIDEO_DESKTOP
        # + inputs["download_size"] * inputs["number_of_downloads"] TODO
    ) / (1024 * 1024)

    smartphone_fixed_line_data_transfer_gb = (
        (
            inputs["smartphone_impressions"] * inputs["product_size"]
            + inputs["video_viewing_time"] * P.MEAN_BITRATE_OF_VIDEO_SMARTPHONE
            + inputs["download_size"] * inputs["number_of_downloads"]
        )
        * (1 - P.SMARTPHONE_MOBILE_NETWORK_SHARE)
    ) / (1024 * 1024)

    smartphone_mobile_line_data_transfer_gb = (
        (
            inputs["smartphone_impressions"] * inputs["product_size"]
            + inputs["video_viewing_time"] * P.MEAN_BITRATE_OF_VIDEO_SMARTPHONE
            + inputs["download_size"] * inputs["number_of_downloads"]
        )
        * (P.SMARTPHONE_MOBILE_NETWORK_SHARE)
    ) / (1024 * 1024)

    tablet_fixed_line_data_transfer_gb = (
        (
            inputs["tablet_impressions"] * inputs["product_size"]
            + inputs["video_viewing_time"] * P.MEAN_BITRATE_OF_VIDEO_TABLET
            + inputs["download_size"] * inputs["number_of_downloads"]
        )
        * (1 - P.TABLET_MOBILE_NETWORK_SHARE)
    ) / (1024 * 1024)

    tablet_mobile_line_data_transfer_gb = (
        (
            inputs["tablet_impressions"] * inputs["product_size"]
            + inputs["video_viewing_time"] * P.MEAN_BITRATE_OF_VIDEO_TABLET
            + inputs["download_size"] * inputs["number_of_downloads"]
        )
        * (P.TABLET_MOBILE_NETWORK_SHARE)
    ) / (1024 * 1024)

    tv_fixed_line_data_transfer_gb = (
        inputs["tv_impressions"] * inputs["product_size"]
        + inputs["video_viewing_time"] * P.MEAN_BITRATE_OF_VIDEO_TV
        # + inputs["download_size"] * inputs["number_of_downloads"] TODO
    ) / (1024 * 1024)

    ereader_fixed_line_data_transfer_gb = (
        inputs["ereader_impressions"]
        * inputs["product_size"]
        # + inputs["download_size"] * inputs["number_of_downloads"] TODO
    ) / (1024 * 1024)

    result["content_delivery_traffic"] = {
        "fixed_line": {
            "laptop": laptop_fixed_line_data_transfer_gb,
            "desktop": desktop_fixed_line_data_transfer_gb,
            "smartphone": smartphone_fixed_line_data_transfer_gb,
            "tablet": tablet_fixed_line_data_transfer_gb,
            "tv": tv_fixed_line_data_transfer_gb,
            "ereader": ereader_fixed_line_data_transfer_gb,
            "total": sum(
                [
                    laptop_fixed_line_data_transfer_gb,
                    desktop_fixed_line_data_transfer_gb,
                    smartphone_fixed_line_data_transfer_gb,
                    tablet_fixed_line_data_transfer_gb,
                    tv_fixed_line_data_transfer_gb,
                    ereader_fixed_line_data_transfer_gb,
                ]
            ),
        },
        "mobile_line": {
            "smartphone": smartphone_mobile_line_data_transfer_gb,
            "tablet": tablet_mobile_line_data_transfer_gb,
            "total": sum(
                [
                    smartphone_mobile_line_data_transfer_gb,
                    tablet_mobile_line_data_transfer_gb,
                ]
            ),
        },
        "cdn": 0,
    }

    result["content_delivery_energy"] = {
        "fixed_line": result["content_delivery_traffic"]["fixed_line"]["total"]
        * P.FIXED_LINE_ENERGY_INTENSITY,
        "mobile_line": result["content_delivery_traffic"]["mobile_line"]["total"]
        * P.MOBILE_LINE_ENERGY_INTENSITY,
    }

    result["content_delivery_emissions"] = {
        "fixed_line": result["content_delivery_energy"]["fixed_line"] * emission_factor,
        "mobile_line": result["content_delivery_energy"]["mobile_line"]
        * emission_factor,
    }

    # CPN
    result["cpn_energy"] = (
        result["content_delivery_traffic"]["fixed_line"]["total"]
        * P.MEAN_ELECTRICAL_ENERGY_USED_BY_CPE_PER_GB
    )
    result["cpn_emissions"] = result["cpn_energy"] * emission_factor

    reporting_period_days = (
        datetime.strptime(inputs["end_date"], "%Y-%m-%d")
        - datetime.strptime(inputs["start_date"], "%Y-%m-%d")
    ).days

    # emission_factor = P.COUNTRY_CARBON_INTENSITY.get(
    #     inputs["country"], P.COUNTRY_CARBON_INTENSITY_DEFAULT
    # )

    return result


# {'product_name': 'test',
#  'product_type': 'website',
#  'country': 'germany',
#  'start_date': '2024-01-01',
#  'end_date': '2024-12-31',
#  'data_center_co2_emissions': '10000',
#  'data_center_energy': '',
#  'data_size': '',
#  'data_center_total_spend': '',
#  'ad_impressions': '650000000',
#  'ad_emission_factor': '29',
#  'product_size': '30700',
#  'time_on_product': '5500000',
#  'video_viewing_time': '0',
#  'number_of_downloads': '0',
#  'download_size': '0',
#  'download_service_time': '0',
#  'computer_impressions': '55000000',
#  'smartphone_impressions': '100000000',
#  'tablet_impressions': '8000000',
#  'tv_impressions': '0',
#  'ereader_impressions': '0'}
