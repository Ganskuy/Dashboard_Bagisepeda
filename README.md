# Bike Sharing Dashboard

An interactive dashboard for analyzing bike rental patterns from the Bike Sharing Dataset. This project is built with Streamlit and summarizes rental performance by date range, weather condition, season, temperature, and humidity.

## Project Overview

This dashboard uses historical bike rental data from Capital Bikeshare, Washington D.C. for 2011-2012. The main dataset used by the app is `all_df.csv`, which is the processed data prepared from the daily and hourly datasets.

Main dashboard features:

- Date range filtering from the sidebar.
- Total bike rentals for the selected period.
- Estimated revenue using an assumption of IDR 10,000 per renter.
- Daily rental trend visualization.
- Temperature and humidity comparison against rental counts.
- Total rental comparison by weather condition.
- Total rental comparison by season.
- Maximum daily rental count for the selected period.

## File Structure

```text
.
├── dashboard.py                  # Streamlit dashboard application
├── Proyek_Analisis_Data.ipynb    # Exploratory data analysis notebook
├── all_df.csv                    # Processed dataset used by the dashboard
├── day.csv                       # Daily aggregated dataset
├── hour.csv                      # Hourly aggregated dataset
├── penamaan_pada_data.txt        # Dataset attribute documentation
├── requirements.txt              # Python dependencies
└── link.txt                      # Published dashboard link
```

## Run the Dashboard Locally

Make sure Python is installed. This project is recommended to run with Python 3.9 or another version compatible with the packages listed in `requirements.txt`.

### 1. Go to the project folder

```sh
cd "/Users/haifanghani/Library/Mobile Documents/com~apple~CloudDocs/Tugas Dicoding/ProyekAkhir_1"
```

If you are running the project from another location, adjust the path to match where the project is stored on your machine.

### 2. Create and activate a virtual environment

Using `venv`:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Or using Conda:

```sh
conda create --name bike-sharing-dashboard python=3.9
conda activate bike-sharing-dashboard
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```sh
streamlit run dashboard.py
```

After the command runs, Streamlit will show a local URL such as:

```text
http://localhost:8501
```

Open that URL in your browser to use the dashboard.

## Important Notes

- Run `streamlit run dashboard.py` from the project root folder so the app can read `all_df.csv`.
- If the app fails to load the dataset, make sure `all_df.csv` is in the same folder as `dashboard.py`.
- The published dashboard link is available in `link.txt`.

## Dataset

The dataset comes from the Bike Sharing Dataset by Hadi Fanaee-T and Joao Gama. It contains bike rental records influenced by time, weather, season, temperature, humidity, working days, and holidays.

Reference:

Fanaee-T, Hadi, and Gama, Joao. "Event labeling combining ensemble detectors and background knowledge." Progress in Artificial Intelligence, 2013.
