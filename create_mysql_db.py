import re

import pymysql
from decouple import config


def main():
    database_name = config('DB_NAME')
    if not re.fullmatch(r'[A-Za-z0-9_]+', database_name):
        raise ValueError('DB_NAME may contain only letters, numbers, and underscores.')

    connection = pymysql.connect(
        host=config('DB_HOST', default='localhost'),
        port=config('DB_PORT', default=3306, cast=int),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        charset='utf8mb4',
        autocommit=True,
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
