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

def get_post(post_id):
    open()
    cursor.execute('''SELECT * from posts WHERE id == (?)''', [post_id])
    post = cursor.fetchone()
    conn.commit()
    close()
    return post

def get_posts():
    open()
    cursor.execute('''
    SELECT * from posts''')
    posts = cursor.fetchall()
    conn.commit()
    close()
    return posts

def get_category_name(id):
    open()
    cursor.execute('''SELECT name from category WHERE id == (?)''', [id])
    category = cursor.fetchone()
    conn.commit()
    close()
    return category

def get_category_post(id):
    open()
    cursor.execute('''SELECT * from posts WHERE category_id == (?)''', [id])
    post = cursor.fetchall()
    conn.commit()
    close()
    return post

def get_categorys():
    open()
    cursor.execute('''SELECT * from category''')
    data = cursor.fetchall()
    conn.commit()
    close()
    return data

def add_post(*data):
    open()
    cursor.execute('''
    INSERT INTO posts (category_id, title, text, image) VALUES ((?), (?), (?), (?))''', 
    [data[0],data[1],data[2],data[3]])
    conn.commit()
    close()
