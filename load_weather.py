import pandas as pd
from google.cloud import bigquery
from google.api_core.exceptions import Conflict

from config import WEATHER_DATASET_NAME, WEATHER_TABLE_NAME, WEATHER_CSV_OUTPUT


def load_weather_to_bigquery(df):
    client = bigquery.Client()

    dataset_id = f"{client.project}.{WEATHER_DATASET_NAME}"
    table_id = f"{client.project}.{WEATHER_DATASET_NAME}.{WEATHER_TABLE_NAME}"

    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"

    try:
        client.create_dataset(dataset, timeout=30)
        print(f"Created dataset {dataset_id}")
    except Conflict:
        print(f"Dataset {dataset_id} already exists, skipping creation.")

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()

    print(f"Loaded {job.output_rows} rows into {table_id}")


if __name__ == "__main__":
    df = pd.read_csv(WEATHER_CSV_OUTPUT)
    load_weather_to_bigquery(df)