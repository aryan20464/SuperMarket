import sqlite3
import os
import random
from insert_items import insert_items
from view_details import view_items
from view_bills import view_bills
from modify_items import modify_items

D_BASE_URL = "/home/chakri/SQLite/smarket_db.sqlite"


def billing_items():
    items_temp = list()
    item_qty_temp = list()
    total_bill = 0
    customer_id_local = 0
    x, i_count = True, 0
    b_number = random.randrange(1, 99999)
    customer_name = raw_input("Enter customer name")
    customer_type = int(raw_input("Are you new customer ? "))

    conn = sqlite3.connect(D_BASE_URL)
    cr = conn.cursor()

    if customer_type == 1:
        cr.execute("insert into customer(name) values (?) ", (customer_name,))

    cr.execute("select id from customer where name = (?)", (customer_name,))
    customer_id_local = cr.fetchone()[0]
    print customer_id_local
    cr.execute("insert into invoice(customer_id, invoice_number) values (?,?)", (customer_id_local, b_number))
    conn.commit()
    conn.close()

    conn1 = sqlite3.connect(D_BASE_URL)
    cur1 = conn1.cursor()
    while x:
        i_count += 1
        i_temp = input("Enter item-ID : ")
        i_quantity = input("Enter Quantity : ")
        cur1.execute('''insert into invoice_items(invoice_id, item_id, quantity) values (?, ?, ?)''',
                     (b_number, i_temp, i_quantity))
        items_temp.append(i_temp)
        item_qty_temp.append(i_quantity)
        if i_count == 2:
            x = False

    conn1.commit()
    conn1.close()

    # print customer_name, "Items \n"


    conn_local = sqlite3.connect(D_BASE_URL)

    price_temp = list()
    name_temp = list()
    for x in range(0, len(items_temp)):
        cur_bill = conn_local.cursor()
        csr = cur_bill.execute('''SELECT item_name, item_price FROM items WHERE item_id = ?''', (items_temp[x],))
        for row in csr:
            # print items_temp[x], row[0], row[1]
            price_temp.insert(x, row[1])
            name_temp.insert(x, row[0])

    print "*" * 70
    print "\nCustomer : ", customer_name, " ID : ", customer_id_local, " Invoice Number : ", b_number, "\n"

    print "\nSno\t\tItem\t\t\t\tPrice\t\tQuantity\t\tFinal Price\n"

    for x in range(0, len(items_temp)):
        total_bill += item_qty_temp[x]*price_temp[x]
        print "%3d \t%-10s \t\t %5d \t\t\t %2.1f \t\t\t%5d" % (x+1, name_temp[x], price_temp[x], item_qty_temp[x],
                                                               item_qty_temp[x]*price_temp[x])

    print "\nTotal : ", total_bill
    print "*" * 70,
    print "\n"

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

# '''-------------------------------------------MAIN PROGRAM STARTS HERE-----------------------------------------------'''
#
# print '''\n\n*********************\n\tChoice \n*********************\
# \n 1. Insert items \n 2. Billing \n 3. View Items
#  4. View Bills \n 5. Modify Items \n*********************\n'''
#
# choice = int(input("Enter the choice : "))
#
# if choice == 1:
#     insert_items()
# elif choice == 2:
#     view_items()
#     billing_items()
# elif choice == 3:
#     view_items()
# elif choice == 4:
#     view_bills()
# elif choice == 5:
#     modify_items()





