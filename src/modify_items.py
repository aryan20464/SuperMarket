import sqlite3
from view_details import view_items

D_BASE_URL = "/home/chakri/SQLite/smarket_db.sqlite"


def modify_items():
    connection_db = sqlite3.connect(D_BASE_URL)
    modify_csr = connection_db.cursor()
    view_items()
    itemid_local = int(raw_input("Enter Item Id "))
    print modify_csr.execute('''select * from items where item_id = ? ''', (itemid_local, )).fetchone()
    choice = int(input("Wanna change \n 1. Name\n 2. Price\n "))
    if choice == 1:
        new_item_name = str(raw_input("Enter New name : "))
        modify_csr.execute("update items set item_name = ? where item_id = ?", (new_item_name, itemid_local))
        connection_db.commit()
        print modify_csr.execute('''select * from items where item_id = ? ''', (itemid_local,)).fetchone()
    elif choice == 2:
        new_item_price = float(input("Enter New price : "))
        modify_csr.execute("update items set item_price = ? where item_id = ?", (new_item_price, itemid_local))
        connection_db.commit()
        print modify_csr.execute('''select * from items where item_id = ? ''', (itemid_local,)).fetchone()
    else:
        print "Wrong input"

    connection_db.close()
