import sqlite3


def view_items():
    conn_local = sqlite3.connect("/home/chakri/SQLite/smarket_db.sqlite")
    cur_bill = conn_local.cursor()
    csr = cur_bill.execute('''SELECT * FROM items''')
    print "\nId\t\tName\t\t\t\tPrice\n"
    for row in csr:
        print "%3d \t%-10s \t\t %5d" % (row[0], row[1], row[2])