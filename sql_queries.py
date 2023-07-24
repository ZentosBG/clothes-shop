import sqlite3


def open():
    global conn, cursor
    conn = sqlite3.connect("sait.db")
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()


def add_category(data):
    open()
    cursor.execute('''
    INSERT INTO category (name) VALUES ((?))''', [data])
    conn.commit()
    close()

def add_user(*data):
    open()
    cursor.execute('''
    INSERT INTO User (name, email, password) VALUES ((?), (?), (?))
    ''', [data[0],data[1],data[2]])
    conn.commit()
    close()

# add_category("skretsh")
# add_user("Roma", "uscdjjdcuc@eeed", "17745")

def get_item(item_id):
    open()
    cursor.execute('''SELECT * from ofers WHERE id == (?)''', [item_id])
    item = cursor.fetchone()
    conn.commit()
    close()
    return item

def get_ofers():
    open()
    cursor.execute('''
    SELECT * from ofers''')
    ofers = cursor.fetchall()
    conn.commit()
    close()
    return ofers

def get_category_name(id):
    open()
    cursor.execute('''SELECT name from category WHERE id == (?)''', [id])
    category = cursor.fetchone()
    conn.commit()
    close()
    return category

def get_category_items(id):
    open()
    cursor.execute('''SELECT * from ofers WHERE category_id == (?)''', [id])
    items = cursor.fetchall()
    conn.commit()
    close()
    return items

def get_categorys():
    open()
    cursor.execute('''SELECT * from category''')
    data = cursor.fetchall()
    conn.commit()
    close()
    return data

def add_order(*data):
    open()
    cursor.execute('''
    INSERT INTO orders (ofers_id, name, phone, email, city, address, amount) VALUES ((?), (?), (?), (?), (?), (?), (?))''', 
    [data[0],data[1],data[2],data[3],data[4],data[5],data[6]])
    conn.commit()
    close()
