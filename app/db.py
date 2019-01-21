import psycopg2
import psycopg2.extras
import os


class DatabaseConnection:
    def __init__(self):

        self.db_name = 'reporti'

        self.connection = psycopg2.connect(
                dbname=self.db_name, user='postgres', host='localhost', password='test', port=5432)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        print('Connected to the database successfully.')
        print(self.db_name)

        create_users_table = "CREATE TABLE IF NOT EXISTS users (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL, othernames VARCHAR NOT NULL,username TEXT NOT NULL, email TEXT NOT NULL, phoneNumber INTEGER NOT NULL, isAdmin BOOLEAN NOT NULL, password TEXT NOT NULL);"

        self.cursor.execute(create_users_table)
if __name__ == '__main__':
    db_name = DatabaseConnection()