import sqlite3


def insert_items():
    item_name_local = str(raw_input("Enter Item name : "))
    item_price_local = int(raw_input("Enter Item Price : "))
    conn_local = sqlite3.connect("/home/chakri/SQLite/smarket_db.sqlite")
    cur_bill = conn_local.cursor()
    cur_bill.execute('''INSERT INTO items(item_name, item_price) VALUES (?, ?)''', (item_name_local, item_price_local))
    f_choice = int(raw_input("Want to enter another item"))
    conn_local.commit()
    if f_choice:
        insert_items()