import sqlite3

def create_table(database,table_name,**columns):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    q_str =''
    for c, t in columns.items():
        q_str += '{} {}, '.format(c, t)
    q_str = q_str[:-2]
    cursor.execute('create table ' + table_name + '(' + q_str + ')')

    db.commit()
    db.close()

def insert(database,table_name,**columns):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    q_str =''
    value_str = ''
    for c, t in columns.items():
        q_str += "{}, ".format(c)
        value_str += "'{}', ".format(t)
    q_str = q_str[:-2]
    value_str = value_str[:-2]
    print(q_str)
    print(value_str)
    sql = 'Insert into ' + table_name + '('+ q_str +') Values(' + value_str + ')'
    print(sql)
    cursor.execute(sql)

    sql = 'select * from student'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    db.commit()
    db.close()

def select(database,table_name,**columns):
    db = sqlite3.connect(database)
    cursor = db.cursor()
    q_str =''
    for c, t in columns.items():
        q_str += "{}='{}' and ".format(c,t)
    q_str = q_str[:-4]
    print(q_str)
    sql = 'select * from ' + table_name + ' Where '+ q_str +''
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()

    print(result)
    db.commit()
    db.close()

