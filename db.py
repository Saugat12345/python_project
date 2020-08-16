import sqlite3
def Customer_Database_Initialiser():
    '''Initialises the database for customers'''
    global conn
    conn = sqlite3.connect('customer.db')
    global c
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS customers(
                first text,
                last text,
                email text,
                age integer,
                username text,
                password text
                )''')
Customer_Database_Initialiser()