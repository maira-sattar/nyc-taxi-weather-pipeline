with taxi_daily as (

    select
        cast(pickup_datetime as date) as trip_date,
        count(*) as total_trips,
        avg(fare_amount) as avg_fare,
        avg(trip_distance) as avg_distance,
        sum(total_amount) as total_revenue

    from {{ ref('stg_taxi_trips') }}
    group by trip_date

),

weather as (

    select
        weather_date,
        temp_max_c,
        temp_min_c,
        precipitation_mm,
        snowfall_cm

    from {{ ref('stg_weather') }}

)

select
    taxi_daily.trip_date,
    taxi_daily.total_trips,
    taxi_daily.avg_fare,
    taxi_daily.avg_distance,
    taxi_daily.total_revenue,
    weather.temp_max_c,
    weather.temp_min_c,
    weather.precipitation_mm,
    weather.snowfall_cm,

    -- a simple derived flag, useful for analysis later
    case
        when weather.precipitation_mm > 0 or weather.snowfall_cm > 0 then true
        else false
    end as is_precipitation_day

from taxi_daily
left join weather
    on taxi_daily.trip_date = weather.weather_date

order by taxi_daily.trip_date