# NYC Taxi & Weather Data Engineering Pipeline

An end-to-end data engineering project that extracts NYC taxi trip data and weather information, transforms and models the data using **Python, dbt, and Apache Airflow**, and loads it into **Google BigQuery**. The pipeline automates the complete ETL workflow using Docker Compose.

## 📌 Project Overview

This project implements an ETL (Extract, Transform, Load) and data modeling pipeline that combines NYC taxi trip records with weather information.

Python scripts handle data extraction and loading, while dbt manages data transformations and modeling within BigQuery. Apache Airflow orchestrates the workflow through a scheduled DAG, ensuring that pipeline tasks execute in the correct sequence.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, Requests |
| Data Transformation | dbt (data build tool) |
| Workflow Orchestration | Apache Airflow |
| Containerization | Docker, Docker Compose |
| Cloud Platform | Google Cloud Platform (GCP) |
| Data Warehouse | Google BigQuery |
| Authentication | Google Cloud IAM Service Account |
| Configuration | Python dotenv |
| Version Control | Git, GitHub |

## 📂 Project Structure

```text
nyc-taxi-weather-pipeline/
│
├── airflow/                    # Airflow DAGs and orchestration scripts
├── logs/                       # Pipeline execution logs
├── taxi_dbt/                   # dbt project for data transformation
│
├── .env                        # Environment variables (not committed)
├── .gitignore                  # Git ignore rules
├── bigquery-credentials.json   # GCP service account credentials (not committed)
├── config.py                   # Configuration settings
│
├── extract.py                  # Extract NYC taxi trip data
├── extract_weather.py          # Extract weather data
├── load.py                     # Load taxi data into BigQuery
├── load_weather.py             # Load weather data into BigQuery
├── pipeline.py                 # Main pipeline execution script
│
├── requirements.txt            # Python dependencies
├── taxi_sample.csv             # Sample NYC taxi dataset
└── weather_sample.csv          # Sample weather dataset
```

## 🔄 Pipeline Workflow

The pipeline consists of four main stages:

### 1. Extract

- Retrieve NYC taxi trip data using `extract.py`.
- Retrieve weather information using `extract_weather.py`.
- Prepare the extracted data for loading into the warehouse.

### 2. Load

- Load NYC taxi trip data into Google BigQuery using `load.py`.
- Load weather data into BigQuery using `load_weather.py`.
- Use the Google Cloud BigQuery Python client for warehouse operations.

### 3. Transform and Model

- Use dbt within the `taxi_dbt/` directory to manage SQL-based transformations.
- Clean and model the raw datasets inside BigQuery.
- Join taxi trip records with weather information where supported by the data and model design.

### 4. Orchestrate

- Use Apache Airflow to coordinate the pipeline tasks through a DAG.
- Execute extraction, loading, and transformation tasks in the required order.
- Configure scheduled execution and monitor task status through the Airflow interface.

## ⚙️ Getting Started

### Prerequisites

Make sure you have the following installed or configured:

- Git
- Python 3.8 or later
- Docker Desktop and Docker Compose
- A Google Cloud Platform project
- BigQuery enabled in your GCP project
- A Google Cloud service account with the required BigQuery permissions

### 1. Clone the Repository

```bash
git clone https://github.com/maira-sattar/nyc-taxi-weather-pipeline.git
```

### 2. Navigate to the Project Directory

```bash
cd nyc-taxi-weather-pipeline
```

### 3. Create a Virtual Environment

Create and activate a Python virtual environment.

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Configure Google Cloud Credentials

1. Create or select a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the BigQuery API.
3. Create a service account with the necessary BigQuery permissions.
4. Generate a JSON key if your authentication setup requires one.
5. Place the credentials file in your project root and configure its path in your environment.

**Important:** Never commit service account keys or other sensitive credentials to GitHub.

### 6. Configure Environment Variables

Create a `.env` file in the project root and add the configuration values required by your scripts.

For example:

```env
GCP_PROJECT_ID=your-gcp-project-id
BIGQUERY_DATASET=your_dataset_name
GOOGLE_APPLICATION_CREDENTIALS=bigquery-credentials.json
```

Replace the example values with your actual configuration. Use the exact variable names expected by `config.py` and your project scripts.

Ensure that `.env` and `bigquery-credentials.json` are included in `.gitignore`.

### 7. Start the Airflow Environment

If your project includes a Docker Compose configuration for Airflow, start the services using:

```bash
docker compose up -d
```

Follow the Airflow setup instructions configured in your repository to initialize the environment and access the Airflow web interface.

**Note:** This command assumes a Docker Compose configuration file is present in the project. If your configuration is stored in another directory, run the command from the appropriate location or specify the Compose file.

### 8. Run the Pipeline

The pipeline can be executed through the main Python script if its dependencies and configuration are set up:

```bash
python pipeline.py
```

⭐ If you find this project useful, consider giving the repository a star!
