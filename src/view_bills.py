import sqlite3

D_BASE_URL = "/home/chakri/SQLite/smarket_db.sqlite"


def view_bills():
    connection_db = sqlite3.connect(D_BASE_URL)
    csr = connection_db.cursor()
    customer_name = str(raw_input("Enter the customer name : "))
    if csr.execute('''select * from customer where customer.name = ?''', (customer_name, )).fetchone() is not None:
        records = csr.execute('''select invoice_items.invoice_id, invoice_items.item_id, items.item_name, invoice_items.quantity, items.item_price,
                    (invoice_items.quantity * items.item_price) as Price from customer join items join invoice_items join invoice
                     on invoice.invoice_number = invoice_items.invoice_id and invoice.customer_id = customer.id and
                     items.item_id = invoice_items.item_id and customer.name= (?)
                     ''', (customer_name,))
        print "InvoiceID  ItemID \t\tItem Name\t\t\t Quantity \t\tPrice(Each) \t\tTotal\n"

        # for normal print without formatting

        '''for row in records:
            for ite in range(0, len(row)):
                print type(row[ite])
                print row[ite],
            print "\n" '''
        for row in records:
            print "%d \t\t %d \t\t\t %-10s \t\t\t %-4.2f \t\t\t %d \t\t\t %-10.2f \n" % (row[0], row[1], row[2], row[3], row[4], row[5])

    else:
        print " *******Customer Not found ********"




