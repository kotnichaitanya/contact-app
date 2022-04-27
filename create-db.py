import sqlite3
db = sqlite3.connect('contact.db')
cursor = db.cursor()

cursor.execute('create table if not exists contact(name text, email text,phoneno text)')

db.commit()
db.close()