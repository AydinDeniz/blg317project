import os
import sys
import psycopg2 as dbapi2

queryList = [
    """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        status VARCHAR(255) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hashes(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        filetype VARCHAR(255) NOT NULL,
        dateadded VARCHAR(255) NOT NULL,
        user_id INTEGER REFERENCES users(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS ipaddresses(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        country VARCHAR(255) NOT NULL,
        dateadded VARCHAR(255) NOT NULL,
        user_id INTEGER REFERENCES users(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS urls(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        currentstatus VARCHAR(255) NOT NULL,
        dateadded VARCHAR(255) NOT NULL,
        user_id INTEGER REFERENCES users(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS emails(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        type VARCHAR(255) NOT NULL,
        dateadded VARCHAR(255) NOT NULL,
        user_id INTEGER REFERENCES users(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hash_email_junction(
        id SERIAL PRIMARY KEY,
        hash_id INTEGER REFERENCES hashes(id),
        email_id INTEGER REFERENCES emails(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hash_url_junction(
        id SERIAL PRIMARY KEY,
        hash_id INTEGER REFERENCES hashes(id),
        url_id INTEGER REFERENCES urls(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS url_email_junction(
        id SERIAL PRIMARY KEY,
        url_id INTEGER REFERENCES urls(id),
        email_id INTEGER REFERENCES emails(id)
    )
    """
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for query in queryList:
            cursor.execute(query)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Error")
        sys.exit(1)
    initialize(url)