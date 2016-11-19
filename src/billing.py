import sqlite3
import os
from insert_items import insert_items
from view_details import view_items


def billing_items():
    items_temp = list()
    item_qty_temp = list()
    total_bill = 0
    x, i_count = True, 0
    customer_name = raw_input("Enter customer name")

    while x:
        i_count += 1
        i_temp = input("Enter item-ID : ")
        i_quantity = input("Enter Quantity : ")
        items_temp.append(i_temp)
        item_qty_temp.append(i_quantity)
        if i_count == 2:
            x = False

    print customer_name, "Items \n"

    conn_local = sqlite3.connect("/home/chakri/SQLite/smarket_db.sqlite")

    price_temp = list()
    name_temp = list()
    for x in range(0, len(items_temp)):
        cur_bill = conn_local.cursor()
        csr = cur_bill.execute('''SELECT item_name, item_price FROM items WHERE item_id = ?''', (items_temp[x],))
        for row in csr:
            # print items_temp[x], row[0], row[1]
            price_temp.insert(x, row[1])
            name_temp.insert(x, row[0])

    print "\nSno\t\tItem\t\t\t\tPrice\t\tQuantity\t\tFinal Price\n"

    for x in range(0, len(items_temp)):
        total_bill += item_qty_temp[x]*price_temp[x]
        print "%3d \t%-10s \t\t %5d \t\t\t %2.1f \t\t\t%5d" % (x+1, name_temp[x], price_temp[x], item_qty_temp[x], item_qty_temp[x]*price_temp[x])

    print "\n\tTotal : ", total_bill

    # for creating files as a database
    '''furl = "/home/chakri/PycharmProjects/SuperMarket/Supermarket_Files/" + customer_name + ".csv"

    if not os.path.exists("/home/chakri/PycharmProjects/SuperMarket/Supermarket_Files"):
        os.makedirs("/home/chakri/PycharmProjects/SuperMarket/Supermarket_Files")

    fop = open(furl, "w")

    fop.write("%s;%s;%s;%s;%s;" % ("Sno", "Item", "Price", "Quantity", "Final Price"))
    fop.write("\n")
    for x in range(0, len(items_temp)):
        fop.write("%d;%s;%d;%f;%d;" % (x + 1, name_temp[x], price_temp[x], item_qty_temp[x], item_qty_temp[x] * price_temp[x]))
        fop.write("\n")
    fop.write("%s;%d" % ("Total", total_bill))
    fop.close()'''


print "Choice \n 1. Insert items \n 2. Billing \n 3. View Items \n"

choice = int(input("Enter the choice : "))

if choice == 1:
    insert_items()
elif choice == 2:
    view_items()
    billing_items()
elif choice == 3:
    view_items()





