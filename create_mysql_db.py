import re

import MySQLdb
from decouple import config


def main():
    database_name = config('DB_NAME')
    if not re.fullmatch(r'[A-Za-z0-9_]+', database_name):
        raise ValueError('DB_NAME may contain only letters, numbers, and underscores.')

    ssl_options = {}
    if config('DB_SSL', default=False, cast=bool):
        ssl_options['ssl'] = {}
        ssl_ca = config('DB_SSL_CA', default='')
        if ssl_ca:
            ssl_options['ssl']['ca'] = ssl_ca

    connection = MySQLdb.connect(
        host=config('DB_HOST', default='localhost'),
        port=config('DB_PORT', default=3306, cast=int),
        user=config('DB_USER', default='root'),
        passwd=config('DB_PASSWORD', default=''),
        charset='utf8mb4',
        autocommit=True,
        **ssl_options,
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{database_name}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
    finally:
        connection.close()

    print(f"Database '{database_name}' is ready.")


if __name__ == '__main__':
    main()
