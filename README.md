# Yetanother-cryptocurrency-pipeline (for everyone)


### Basic pipeline template for cryptocurrency.

<picture width="500">
  <img
    width="600"
    src="https://github.com/klchkvdnl/yetanother-cryptocurrency-pipeline/blob/master/pipeline-image.png"
    alt="Pipeline inage (light)"
  />
</picture>

### Components

- [superset 5.0.0](https://github.com/apache/superset/tree/4ed05f4ff16805b1253a902172a53e973cf41f1e)
- [airflow 3.1.6](https://hub.docker.com/layers/apache/airflow/3.1.6/images/sha256-18a9758b0b6d69bb761400507ba3163bad52a5d447fb9f331c56beffb91ad104)
- [postgres 17](https://github.com/docker-library/postgres/blob/9451a9a586c4c0efc0fc7c31afbe36d9d650c137/17/alpine3.23/Dockerfile)
- [dbt-postgres 1.9.latest](https://github.com/dbt-labs/dbt-core/pkgs/container/dbt-postgres)

### Short description for pipeline



### Main resource

Basic data source is CoinGecko Demo API:
https://docs.coingecko.com/v3.0.1/reference/authentication

(but it can be anything)

### installation
- first of all install docker and uv python package-manager
- download repo and open it
- use `uv sync`
- open `./api_request/api_request.py` 
    - add your API_KEY
- open `./airflow/dags/orchestrator.py` 
    - change paths for mount directory inside docker operator
- start docker `docker-compose up`
- open airflow on `http://localhost:8000/` and run dag
- open superset on `http://localhost:8088/` and tune your dashboard
    - by default mart layer contains only data for bitcoin