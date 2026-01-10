import sqlite3


class DataBase:
    def __init__(self, db_name="main.db"):
        self.db_name = db_name
        self.create_tables()
        self.insert_default_foods()

    def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql, args)

            if commit:
                db.commit()

            result = None
            if fetchone:
                result = cursor.fetchone()
            elif fetchall:
                result = cursor.fetchall()

        return result

    def create_tables(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            full_name TEXT,
            phone TEXT
        )
        """

        sqlfood = """
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        )
        """

        sqlorders = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            food TEXT,
            quantity INTEGER,
            status TEXT
        )
        """

        self.manager(sql, commit=True)
        self.manager(sqlfood, commit=True)
        self.manager(sqlorders, commit=True)

    def insert_users(self,telegram_id,full_name,phone):
        sql = """INSERT INTO (telegram_id,full_name, phone) VALUES (?,?)"""

        self.manager(sql,(telegram_id,full_name,phone), commit=True)

db = DataBase()