import sqlite3

D_BASE_URL = "/home/chakri/SQLite/smarket_db.sqlite"

connection_basic = sqlite3.connect(D_BASE_URL)
cur = connection_basic.cursor()

cur.executescript('''
create table if not exists customer(id integer not null primary key autoincrement unique, name text);
CREATE TABLE if not exists items(item_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, item_name TEXT UNIQUE, item_price INTEGER);;
create table if not exists invoice (customer_id integer, invoice_number integer);
create table if not exists invoice_items(invoice_id integer, item_id integer, quantity float);
''')

connection_basic.commit()
connection_basic.close()