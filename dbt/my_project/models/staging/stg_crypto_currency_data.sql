{{ config(
    materialized='table',
    unique_key='id'
)}}

with source as (
    select 
        json_array_elements(json_data) AS coin_info
        , inserted_at
    from {{ source('dev', 'raw_crypto_currency_data')}}
)

select
    coin_info->>'id' AS id,
    coin_info->>'symbol' AS symbol,
    (coin_info->>'current_price')::real AS current_price,
    (coin_info->>'market_cap')::int8 AS market_cap,
    (coin_info->>'total_volume')::int8 AS total_volume,
    (coin_info->>'last_updated')::timestamp AS last_updated,
    inserted_at
from source