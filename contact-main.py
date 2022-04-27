from contact import contact
import sqlite3

def add_contact(contact):
    db = sqlite3.connect('contact.db')
    cursor = db.cursor()
    sql = 'select * from contact where phoneno='+'\''+contact.phoneno+'\' or email='+'\''+contact.email+'\''
    result = cursor.execute(sql)
    result = cursor.fetchall()

    if not result:
        cursor.execute('insert into contact values(?,?,?)', (contact.name, contact.email, contact.phoneno))
    else:
        print('Already the email or phone-no exists')
    
    db.commit()
    db.close()

def ListContacts():
    db = sqlite3.connect('contact.db')
    cursor = db.cursor()
    cursor.execute('select * from contact')
    result = cursor.fetchall()
    printContacts(result)
    #print(result)
    db.commit()
    db.close()

def searchbyName(name):
    db = sqlite3.connect('contact.db')
    cursor = db.cursor()
    sql = 'select * from contact where name ='+'\''+name+'\''
    cursor.execute(sql)
    result = cursor.fetchall()
    printContacts(result)
    db.commit()
    db.close()

def searchbyNumber(number):
    db = sqlite3.connect('contact.db')
    cursor = db.cursor()
    sql = 'select * from contact where phoneno ='+'\''+number+'\''
    cursor.execute(sql)
    result = cursor.fetchall()
    printContacts(result)
    db.commit()
    db.close()

def printContacts(results):
    print()
    print('┌====================================================┐')
    print('| Name \t\t     Email \t\t   phoneNo   |')
    print('|====================================================|')
    for result in results:
        print('| {} \t {}  {}  |'.format(result[0],result[1],result[2]))
    print('└====================================================┘')
    print()

while True:

    print('\nAll Choices\n1.Add Contact\n2.Edit name using mail\n3.Edit Number using mail\n4.Search using Name\n5.Search using PhoneNumber\n6.Display All Contacts\n7.Delete\n8.Exit\n')
    case_value = int(input('Enter the Option :'))
    
    if case_value == 1:
        name = input('Enter the Name:')
        email = input('Enter the Email:')
        phoneno = input('Enter the Number:')
        contact_obj = contact(name,email,phoneno)
        add_contact(contact_obj)
 
    elif case_value == 2:
        email = input('Enter the Email to edit name of contact:')
        db = sqlite3.connect('contact.db')
        cursor = db.cursor()
        sql = 'select * from contact where email ='+'\''+email+'\''
        cursor.execute(sql)
        result = cursor.fetchall()
        if not result:
            print('No Email Found Please check Again')
        else:
            name = input('Enter the Name to Update:')
            sql = 'Update contact set name ='+'\''+name+'\' where email='+'\''+email+'\''
            cursor.execute(sql)
        db.commit()
        db.close()

    elif case_value == 3:
        email = input('Enter the Email to edit Number:')
        db = sqlite3.connect('contact.db')
        cursor = db.cursor()
        sql = 'select * from contact where email ='+'\''+email+'\''
        cursor.execute(sql)
        result = cursor.fetchall()
        if not result:
            print('No Email Found Please check Again')
        else:
            number = input('Enter the number to Update:')
            sql = 'Update contact set phoneno ='+'\''+number+'\' where email='+'\''+email+'\''
            cursor.execute(sql)
        db.commit()
        db.close()

    elif case_value == 4:
        name = input('Enter the Name to Search :')
        searchbyName(name)

    elif case_value == 5:
        number = input('Enter the Number to Search :')
        searchbyNumber(number)

    elif case_value == 6:
        ListContacts()
        
    elif case_value == 7:
        email = input('Enter the Email to delete Contact:')
        db = sqlite3.connect('contact.db')
        cursor = db.cursor()
        sql = 'delete from contact where email ='+'\''+email+'\''
        cursor.execute(sql)
        print('Deletion Success')
        db.commit()
        db.close()

    elif case_value == 8:
        exit()
        
    else:
        print("Please check The Option Entered")






