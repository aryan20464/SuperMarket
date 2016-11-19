import sqlite3

connection_basic = sqlite3.connect("/home/chakri/SQLite/smarket_db.sqlite")
cur = connection_basic.cursor()

cur.executescript('''

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS items;

CREATE TABLE users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT);
CREATE TABLE items(item_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, item_name TEXT, item_price INTEGER);
''')

connection_basic.commit()