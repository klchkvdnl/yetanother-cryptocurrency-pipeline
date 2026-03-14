{{ config(
    materialized='table',
    unique_key='id'
)}}

select *
from {{ ref('stg_crypto_currency_data')}}
where id = 'bitcoin'