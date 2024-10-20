import sqlite3

with sqlite3.connect('../database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students;')
    print(cursor.fetchall())
    conn.commit()