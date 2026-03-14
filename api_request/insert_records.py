import logging

import psycopg2

from api_request import get_crypto_currency_list
from api_request import mock_fetch_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

def connect_to_db():
    logger.info('Connecting to postgres db...')
    try:
        conn = psycopg2.connect(
            dbname='db',
            user='db_user',
            password='db_password',
            port='5432',
            host='db'
        )
        logger.info('Connection successful.')
        return conn
    except psycopg2.Error as e:
        logger.info(f'Connection to postgres db failed. Error: {e}')
        raise

def create_table_if_not_exist(conn):
    logger.info('Creating new table if not exist...')
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_crypto_currency_data (
                id SERIAL PRIMARY KEY,
                json_data JSON,
                inserted_at TIMESTAMP DEFAULT NOW()
                );
        """)
        conn.commit()
        logger.info('Table was created.')
    except psycopg2.Error as e:
        logger.info(f'Creating new table failed. Error: {e}')
        raise

def insert_records(conn, data):
    logger.info('Inserting weather data into db...')
    try:
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO dev.raw_crypto_currency_data (
                json_data,
                inserted_at
            ) VALUES ('{data}', NOW());
        """)
        conn.commit()
        logger.info('Data succesfully inserted.')
    except psycopg2.Error as e:
        logger.info(f'Inserting weather data into db failed. Error: {e}')
        raise


def main():
    try:
        data = get_crypto_currency_list()
        # data = mock_fetch_data()
        conn = connect_to_db()
        create_table_if_not_exist(conn)
        insert_records(conn, data)
    except Exception as e:
        logger.info(f'Got an error durring execution. Error: {e}')
    finally:
        if conn in locals():
            conn.close()
            logger.info('DB connection closed.')

if __name__=='__main__':
    main()