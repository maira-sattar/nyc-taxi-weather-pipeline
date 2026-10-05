import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery-credentials.json"

SOCRATA_URL = "https://data.cityofnewyork.us/resource/rwwi-khbc.json"
LIMIT = 50000
MAX_RECORDS = 600000
DATASET_NAME = "taxi_raw"
TABLE_NAME = "trips_2024"
CSV_OUTPUT = "taxi_sample.csv"

# WEATHER CONFIG
WEATHER_DATASET_NAME = "weather_raw"
WEATHER_TABLE_NAME = "nyc_weather_2024"
WEATHER_CSV_OUTPUT = "weather_sample.csv"