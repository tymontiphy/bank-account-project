import sqlite3

DATABASE_NAME = './lib/db/bank_account.db'

class Connection:
    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
        return conn
