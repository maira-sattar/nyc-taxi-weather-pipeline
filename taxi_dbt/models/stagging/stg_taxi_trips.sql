select
    vendorid as vendor_id,
    cast(tpep_pickup_datetime as timestamp) as pickup_datetime,
    cast(tpep_dropoff_datetime as timestamp) as dropoff_datetime,
    passenger_count,    
    trip_distance,
    ratecodeid as rate_code_id,
    pulocationid as pickup_location_id,
    dolocationid as dropoff_location_id,
    payment_type,
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    total_amount
from {{ source('taxi_raw', 'trips_2024') }}

where
 fare_amount > 0
 and trip_distance > 0
 and passenger_count > 0  
 and tpep_pickup_datetime >= '2024-01-01'
 and tpep_pickup_datetime < '2025-01-01'