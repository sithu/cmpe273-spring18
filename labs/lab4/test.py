import sqlite3

import sqlite3
conn = sqlite3.connect('test.db')

def create_table(): 
    c = conn.cursor()
    c.execute('''
            CREATE TABLE person
            (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
            ''')
    conn.commit()
    conn.close()

def test():
    c = conn.cursor()
    c.execute('SELECT * FROM person')
    print(c.fetchall())
    conn.close()

if __name__ == "__main__":
    create_table()
