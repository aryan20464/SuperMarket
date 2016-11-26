import sqlite3
import re

D_BASE_URL = "/home/chakri/SQLite/smarket_db.sqlite"


def view_items():
    conn_local = sqlite3.connect(D_BASE_URL)
    cur_bill = conn_local.cursor()
    csr = cur_bill.execute('''SELECT * FROM items''')
    print "\nId\t\tName\t\t\t\tPrice\n"
    for row in csr:
        print "%3d \t%-10s \t\t %5d" % (row[0], row[1], row[2])


def dbase_results_gui_args(item_param):
    connection_db = sqlite3.connect(D_BASE_URL)
    csr = connection_db.cursor()
    item_param = str(item_param)
    zx = re.match("[0-9]+", item_param)
    if str(item_param) == "ALL":
        records = csr.execute('''select * from items''')
    elif zx is not None:
        records = csr.execute('''select * from items where item_id = ?''', (int(item_param),))
    else:
        records = csr.execute('''select * from items where item_name = ?''', (str(item_param),))
    return records.fetchall()

