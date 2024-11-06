import sqlite3


def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year INTEGER)")
    conn.commit()
    conn.close()


def insert(title,author,year):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book values(Null, ?, ?, ?)", (title,author,year))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM book")
    rows= cur.fetchall()
    conn.close()
    return rows




def search(title="", author="", year=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()


    cur.execute("SELECT * FROM book WHERE Name=? OR Family=? OR Age=?", (title,author,year))

    results = cur.fetchall()
    conn.close()
    return results





def delete(record_id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()


    cur.execute("DELETE FROM book WHERE id=?", (record_id,))


    conn.commit()
    conn.close()




def update(record_id,title,author,year):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()


    cur.execute("UPDATE book SET title=?,author=?, year=? WHERE id=?", (title,author,year, record_id))


    conn.commit()
    conn.close()


connect()