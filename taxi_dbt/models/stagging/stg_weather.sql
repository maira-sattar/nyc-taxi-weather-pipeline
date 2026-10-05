select
    cast(time as date) as weather_date,
    temperature_2m_max as temp_max_c,
    temperature_2m_min as temp_min_c,
    precipitation_sum as precipitation_mm,
    snowfall_sum as snowfall_cm

from {{ source('weather_raw', 'nyc_weather_2024') }}