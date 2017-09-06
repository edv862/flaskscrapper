from flask import Flask, make_response
import csv
from conect_mysql import dbHelper


def getInfo():
    db = dbHelper()
    csvstring = """name,make,model,colour,capacity,image,sku,url,category,subcategory,grade,sellprice,buyprice,voucherprice
"""
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

    while products > 0:
        aux = cur.fetchone()
        csvstring += (str(aux)[1:-1] + '\n').replace('\'', '"')
        products -= 1

    return csvstring


# EB looks for an 'application' callable by default.
application = Flask(__name__)


@application.route('/')
def index():
    csvstring = getInfo()
    response = make_response(csvstring)
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    response.headers["Content-type"] = "text/csv"
    return response


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run()