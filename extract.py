import time
import requests
import pandas as pd

from config import SOCRATA_URL, LIMIT, MAX_RECORDS, CSV_OUTPUT

MAX_RETRIES = 3

def extract_taxi_data():
    all_records = []
    offset = 0

    while offset < MAX_RECORDS:
        params = {
            "$limit": 50000,
            "$offset": offset,
            "$order": "tpep_pickup_datetime",
            "$where": "tpep_pickup_datetime >= '2024-01-01T00:00:00' AND tpep_pickup_datetime < '2024-01-08T00:00:00'"
        }

        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(SOCRATA_URL, params=params, timeout=30)
            except requests.exceptions.RequestException as e:
                print(f"Network error at offset {offset}, attempt {attempt+1}: {e}")
                time.sleep(2 ** attempt)
                continue

            if response.status_code == 200:
                break
            elif response.status_code == 429:
                wait = 2 ** attempt
                print(f"Rate limited at offset {offset}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"Error at offset {offset}: {response.status_code}")
                response = None
                break
        else:
            print(f"Giving up on offset {offset} after {MAX_RETRIES} attempts.")
            break

        if response is None or response.status_code != 200:
            break

        page_data = response.json()

        if not page_data:
            print("No more data available, stopping.")
            break

        all_records.extend(page_data)
        print(f"Pulled {len(page_data)} records, total so far: {len(all_records)}")

        offset += LIMIT
        time.sleep(0.5)

    all_records = all_records[:MAX_RECORDS]
    df = pd.DataFrame(all_records)
    print(f"\nExtraction complete. Final shape: {df.shape}")
    return df


if __name__ == "__main__":
    df = extract_taxi_data()
    df.to_csv(CSV_OUTPUT, index=False)
    print(f"Saved to {CSV_OUTPUT}")