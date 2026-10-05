from config import CSV_OUTPUT
from extract import extract_taxi_data
from load import load_to_bigquery


if __name__ == "__main__":
    df = extract_taxi_data()

    df.to_csv(CSV_OUTPUT, index=False)
    print(f"Saved local backup to {CSV_OUTPUT}")

    load_to_bigquery(df)