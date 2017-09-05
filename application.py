# from flask import Flask, make_response, send_from_directory
# import csv
# from conect_mysql import dbHelper

# def getInfo():
#     db = dbHelper()
#     file = open("data.csv", "w+")
#     c = csv.writer(file)

#     con = db.connect()
#     cur = con.cursor()
#     products = cur.execute(
#         """SELECT p.name, p.make, p.model, p.colour, p.capacity, p.img, p.sku, url.url_dir, cat.name, scat.name, grade.type, price.sell_price, price.buy_price, price.voucher_price
#             FROM product as p
#             LEFT JOIN url ON p.url=url.id
#             LEFT JOIN category AS cat ON p.category=cat.id
#             LEFT JOIN subcategory AS scat ON p.sub_category=scat.id
#             LEFT JOIN grade ON p.grade=grade.id
#             LEFT JOIN price ON p.price=price.id
#             """)

#     c.writerow(['name', 'make', 'model', 'colour', 'capacity', 'image', 'sku', 'url', 'category', 'subcategory', 'grade', 'sellprice', 'buyprice', 'voucherprice'])
#     while products > 0:
#         row = cur.fetchone()
#         c.writerow(row)
#         products -= 1

#     file.close()
#     return file

# # EB looks for an 'application' callable by default.
# application = Flask(__name__)


# @application.route('/')
# def index():
#     getInfo()
#     return send_from_directory(directory='.', filename='data.csv', as_attachment=True)


# # run the app.
# if __name__ == "__main__":
#     # Setting debug to True enables debug output. This line should be
#     # removed before deploying a production app.
#     application.debug = True
#     application.run()
from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()