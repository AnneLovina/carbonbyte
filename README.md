# CarbonByte: Digital Product Carbon Footprint Calculator

## 1. What is CarbonByte?

CarbonByte is a web application designed to help users estimate the carbon footprint of their digital products, such as websites, apps, podcasts, newsletters, or e-papers. Users can input various metrics related to their product's lifecycle, including data center usage, advertising, and end-user interaction. The application then calculates the estimated CO2 emissions associated with these activities over a specified period.

Key features include:
* A web-based calculator interface to input product details and usage data.
* Calculation of emissions across different categories: Data Centers, Advertising, Content Delivery, and End-User Devices.
* User accounts for saving calculation history.
* Ability to download calculation results as PDF or Excel files.
* Visualization of the emissions breakdown.

## 2. Why is this Project Important?

While often perceived as intangible, digital products and services have a real-world environmental impact, primarily driven by the energy consumed throughout their value chain. Data centers, network infrastructure, and the end-user devices accessing these products all require electricity, which contributes to greenhouse gas emissions. CarbonByte aims to bring awareness to this digital carbon footprint, enabling creators and businesses to understand the environmental impact of their digital offerings and make more informed, sustainable choices.

## 3. Methodology

The CarbonByte calculation model estimates CO2 emissions by focusing on the primary energy consumers in the digital value chain:

1.  **Data Center Emissions:** Calculated based on user-provided CO2 emissions data for the data center(s) used.
2.  **Advertising Emissions:** Calculated using the number of ad impressions and an emission factor (either user-provided or a default value from `parameters.py`).
3.  **Content Delivery (Network) Emissions:** Estimated based on the total data transferred (calculated from product size, video viewing time, and downloads) across fixed and mobile networks. It uses energy intensity factors (kWh/GB) for each network type and applies a country-specific carbon intensity factor (kg CO2e/kWh) for electricity.
4.  **End-User Device Emissions:** Calculated based on the time users spend on the product, distributed across different device types (laptops, desktops, smartphones, tablets, TVs, e-readers) according to impression counts. It considers the average power consumption of each device type and the carbon intensity of electricity in the specified country.

**Scope Limitations:**
* The model primarily focuses on the operational energy use of data centers, networks, and end-user devices.
* It does **not** currently include emissions related to:
    * Development and Design phases.
    * Maintenance and Updates (e.g., CI/CD pipelines).
    * Hardware manufacturing (embodied carbon).
    * Product disposal and recycling.

*Constants and Emission Factors:* Default values for energy intensity, device power consumption, data transfer bitrates, and country carbon intensity are defined in `parameters.py`.

## 4. How to Run CarbonByte

Follow these steps to set up and run the CarbonByte application locally:

1.  **Prerequisites:**
    * Python 3.12 installed.
    * `pip` (Python package installer).

2.  **Clone the Repository (if applicable):**
    * If you have the code in a git repository, clone it:
        ```bash
        git clone https://github.com/AnneLovina/carbonbyte.git
        cd carbonbyte
        ```
    * Otherwise, ensure you are in the main `carbonbyte` directory containing the `app.py` file.

3.  **Install Dependencies:**
    * Install the required Python packages listed in `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Database Setup:**
    * The application uses SQLite for the database (`users.db`).
    * The database file will be created automatically in the project directory the first time you run the application.

5.  **Run the Application:**
    * Start the Flask development server:
        ```bash
        python app.py
        ```

6.  **Access CarbonByte:**
    * Open your web browser and navigate to the address provided in the console output, typically `http://127.0.0.1:8080` or `http://0.0.0.0:8080`.

You can now register an account, log in, and use the calculator to estimate the carbon footprint of digital products.
