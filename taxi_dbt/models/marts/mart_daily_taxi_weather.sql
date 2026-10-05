{{ config(materialized='table') }}
select
    trip_date,
    total_trips,
    round(avg_fare, 2) as avg_fare,
    round(avg_distance, 2) as avg_distance,
    round(total_revenue, 2) as total_revenue,
    temp_max_c,
    temp_min_c,
    precipitation_mm,
    snowfall_cm,
    is_precipitation_day,

    -- business-friendly categorical bucket, useful for grouping in dashboards
    case
        when temp_max_c < 0 then 'freezing'
        when temp_max_c < 10 then 'cold'
        when temp_max_c < 20 then 'mild'
        else 'warm'
    end as temperature_category,

    -- day-of-week, useful for spotting weekly patterns
    format_date('%A', trip_date) as day_of_week

from {{ ref('taxi_weather_daily') }}

order by trip_date