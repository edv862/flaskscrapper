from flask import Flask, make_response, send_from_directory
import csv
from conect_mysql import dbHelper

def getInfo():
    db = dbHelper()
    file = open("data.csv", "w+")
    c = csv.writer(file)

    con = db.connect()
    cur = con.cursor()
    products = cur.execute(
        """SELECT p.name, p.make, p.model, p.colour, p.capacity, p.img, p.sku, url.url_dir, cat.name, scat.name, grade.type, price.sell_price, price.buy_price, price.voucher_price
            FROM product as p
            LEFT JOIN url ON p.url=url.id
            LEFT JOIN category AS cat ON p.category=cat.id
            LEFT JOIN subcategory AS scat ON p.sub_category=scat.id
            LEFT JOIN grade ON p.grade=grade.id
            LEFT JOIN price ON p.price=price.id
            """)

    c.writerow(['name', 'make', 'model', 'colour', 'capacity', 'image', 'sku', 'url', 'category', 'subcategory', 'grade', 'sellprice', 'buyprice', 'voucherprice'])
    while products > 0:
        row = cur.fetchone()
        c.writerow(row)
        products -= 1

    file.close()
    return file

# EB looks for an 'application' callable by default.
application = Flask(__name__)


@application.route('/')
def index():
    getInfo()
    return send_from_directory(directory='.', filename='data.csv', as_attachment=True)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
