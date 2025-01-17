import subprocess
import json
from urllib.parse import urlparse
import sys
import time
import tempfile
import os


def get_domain_size_curl(domain):
    """
    Get the size of a webpage using curl with Chrome user agent
    """
    try:
        # Ensure domain has proper scheme
        if not domain.startswith(("http://", "https://")):
            domain = "https://" + domain

        # Create a temporary file to store the output
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_path = tmp_file.name

        curl_command = [
            "curl",
            "-A",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "-L",  # Follow redirects
            "-o",
            tmp_path,  # Output to temporary file
            "-w",
            "%{size_download}",  # Print the download size
            "-s",  # Silent mode
            domain,
        ]

        result = subprocess.run(curl_command, capture_output=True, text=True)

        if result.returncode == 0:
            size = int(result.stdout.strip())
            os.unlink(tmp_path)
            return size
        else:
            print(f"Curl error: {result.stderr}")
            return None

    except Exception as e:
        print(f"Error getting domain size: {str(e)}")
        return None


def get_green_hosting_data_curl(domain):
    """
    Get green hosting information from The Green Web Foundation API using curl
    """
    try:
        # Clean domain (remove protocol and www if present)
        clean_domain = (
            urlparse(domain).netloc.replace("www.", "")
            if domain.startswith(("http://", "https://"))
            else domain.replace("www.", "")
        )

        api_url = (
            f"https://admin.thegreenwebfoundation.org/api/v3/greencheck/{clean_domain}"
        )

        curl_command = [
            "curl",
            "-X",
            "GET",
            "-H",
            "accept: application/json",
            "-s",  # Silent mode
            api_url,
        ]

        result = subprocess.run(curl_command, capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                print(f"Raw response: {result.stdout}")
                return None
        else:
            print(f"Curl error: {result.stderr}")
            return None

    except Exception as e:
        print(f"Error in get_green_hosting_data: {str(e)}")
        return None


def get_similarweb_data(domain):
    """
    Get traffic data from SimilarWeb API using curl with additional headers
    """
    clean_domain = (
        urlparse(domain).netloc.replace("www.", "")
        if domain.startswith(("http://", "https://"))
        else domain.replace("www.", "")
    )
    api_url = f"https://data.similarweb.com/api/v1/data?domain={clean_domain}"

    try:
        # Enhanced headers to better mimic a browser request
        curl_command = [
            "curl",
            "-A",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "-H",
            "Accept: application/json",
            "-H",
            "Accept-Language: en-US,en;q=0.9",
            "-H",
            f"Origin: https://www.similarweb.com",
            "-H",
            f"Referer: https://www.similarweb.com/website/{clean_domain}/",
            "-H",
            "Sec-Fetch-Dest: empty",
            "-H",
            "Sec-Fetch-Mode: cors",
            "-H",
            "Sec-Fetch-Site: same-site",
            "--compressed",
            "-s",  # Silent mode
            api_url,
        ]

        result = subprocess.run(curl_command, capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            try:
                data = json.loads(result.stdout)
                visits = data.get("Engagments", {}).get("Visits")
                if visits:
                    return {
                        "EstimatedMonthlyVisits": {"value": int(float(visits))},
                        "Engagements": data.get("Engagments", {}),
                    }
                else:
                    print("No visits data found in response")
                    return None
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                print(f"Raw response: {result.stdout}")
                return None
        else:
            print(f"Curl command failed: {result.stderr}")
            return None

    except Exception as e:
        print(f"Error in get_similarweb_data: {str(e)}")
        print(f"Type of error: {type(e)}")
        import traceback

        print(f"Traceback: {traceback.format_exc()}")
        return None


def format_size(size_bytes):
    """Format size in bytes to human readable format"""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


def calculate_total_traffic_size(domain):
    """Calculate total traffic size based on page size and visitor count"""
    result = {}

    print(f"\nFetching page size for {domain}...")
    page_size = get_domain_size_curl(domain)
    if page_size is not None:
        result["page_size_bytes"] = page_size
        result["page_size_formatted"] = format_size(page_size)
        print(f"Page size: {result['page_size_formatted']}")

    print("\nWaiting before making SimilarWeb request...")
    time.sleep(2)

    print("Fetching SimilarWeb data...")
    similarweb_data = get_similarweb_data(domain)
    if similarweb_data is not None:
        result["similarweb_data"] = similarweb_data
        try:
            monthly_visits = similarweb_data["EstimatedMonthlyVisits"]["value"]
            result["monthly_visits"] = monthly_visits
            total_traffic = page_size * monthly_visits
            result["total_traffic_bytes"] = total_traffic
            result["total_traffic_formatted"] = format_size(total_traffic)
        except Exception as e:
            print(f"Error calculating traffic: {str(e)}")

    print("\nFetching green hosting data...")
    green_hosting_data = get_green_hosting_data_curl(domain)
    if green_hosting_data is not None:
        result["green_hosting_data"] = green_hosting_data

    result["domain"] = domain
    result["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

    # Add environmental impact indicators
    if "green_hosting_data" in result:
        result["environmental_indicators"] = {
            "green_hosted": result["green_hosting_data"].get("green", False),
            "hosting_provider": result["green_hosting_data"].get("hosted_by"),
            "provider_website": result["green_hosting_data"].get("hosted_by_website"),
            "supporting_documents": result["green_hosting_data"].get(
                "supporting_documents", []
            ),
        }

    return result if result else None


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py domain.com")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"Analyzing domain: {domain}")

    result = calculate_total_traffic_size(domain)
    if result:
        # Save results to JSON file
        output_filename = (
            f"{domain.replace('/', '_')}_analysis_{time.strftime('%Y%m%d_%H%M%S')}.json"
        )
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print("\nResults:")
        if "page_size_formatted" in result:
            print(
                f"Page Size: {result['page_size_formatted']} ({result['page_size_bytes']:,} bytes)"
            )
        if "monthly_visits" in result:
            print(f"Monthly Visits: {result['monthly_visits']:,}")
        if "total_traffic_formatted" in result:
            print(f"Total Monthly Traffic: {result['total_traffic_formatted']}")
        if "green_hosting_data" in result:
            print(f"\nGreen Hosting Status:")
            print(
                f"Provider: {result['green_hosting_data'].get('hosted_by', 'Unknown')}"
            )
            print(f"Green Hosted: {result['green_hosting_data'].get('green', False)}")
            if result["green_hosting_data"].get("supporting_documents"):
                print(
                    f"Supporting Documents Available: {len(result['green_hosting_data']['supporting_documents'])}"
                )

        print(f"\nDetailed results saved to: {output_filename}")
    else:
        print("Failed to analyze domain")


if __name__ == "__main__":
    main()
