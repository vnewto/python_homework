# **Task 1: Create a New SQLite Database**
import sqlite3

with sqlite3.connect('../db/magazines.db') as conn:
    print('Database created and connected successfully')


# **Task 2: Define Database Structure**
with sqlite3.connect('../db/magazines.db') as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    #create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        pub_id INTEGER PRIMARY KEY,
        pub_name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        mag_id INTEGER PRIMARY KEY,
        mag_name TEXT NOT NULL UNIQUE,
        pub_name TEXT NOT NULL,
        pub_id INTEGER,
        FOREIGN KEY (pub_id) REFERENCES Publishers (pub_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        sub_id INTEGER PRIMARY KEY,
        sub_name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        expiration_date TEXT NOT NULL,
        sub_id INTEGER,
        mag_id INTEGER,
        pub_id INTEGER,
        FOREIGN KEY (sub_id) REFERENCES Subscribers (sub_id),
        FOREIGN KEY (mag_id) REFERENCES Magazines (mag_id)
    )
    """)

    print("Tables created successfully.")


# **Task 3: Populate Tables with Data**

    #function to add a publisher
    def add_publisher(cursor, publisher_name):
        try:
            cursor.execute("INSERT INTO Publishers (pub_name) VALUES (?)", [publisher_name])
        except sqlite3.IntegrityError:
            print(f"{publisher_name} is already in the database.")
    
    #function to add a magazine
    def add_magazine(cursor, magazine_name, publisher):
        try:
            #search the publisher's table to make sure publisher exists
            cursor.execute("SELECT * FROM Publishers WHERE pub_name = ?", [publisher])
            results = cursor.fetchall()
            #if doesn't exist, print error message and exit
            if len(results) == 0:
                print(f"The publisher {publisher} does not exist. ")
                return
            #if does exist, pull pub_id from the table and add data to table
            else: 
                pub_id = results[0][0] 
                cursor.execute("INSERT INTO Magazines (mag_name, pub_name, pub_id) VALUES (?, ?, ?)", [magazine_name, publisher, pub_id])          
        except sqlite3.IntegrityError:
            print(f"{magazine_name} is already in the database.")
    
    #function to add a subscriber
    def add_subscriber(cursor, name, address):
        try:
            #first check for duplicates
            cursor.execute("SELECT * FROM Subscribers WHERE sub_name = ? AND address = ?", (name, address))
            results = cursor.fetchall()
            if len(results) > 0:
                   print(f"{name}, {address} is already in the database.")
                   return
            #if no duplicates, add subscriber to table
            else:
                cursor.execute("INSERT INTO Subscribers (sub_name, address) VALUES (?, ?)", [name, address])
        except sqlite3.Error as e:
            print(f"(A SQL error occured: {e})")
    
    #function to add a subscription
    def subscribe(cursor, name, address, magazine_name, expiration_date):
        try:
            #check for name and address and pull sub_id from subscriber table
            cursor.execute("SELECT * FROM Subscribers WHERE sub_name = ? AND address = ?", [name, address])
            results = cursor.fetchall()
            if len(results) > 0:
                sub_id = results[0][0]            
            else:
                print(f"There was no subscriber named {name} at {address}.")
                return
            
            #check for magazine name and pull mag_id from magazine table
            cursor.execute("SELECT * FROM Magazines WHERE mag_name = ?", [magazine_name])
            results = cursor.fetchall()
            if len(results) > 0:
                mag_id = results[0][0]
            else: 
                print(f"There was no magazine named {magazine_name}.")
                return

            #check for duplicates in the subscription table
            cursor.execute("SELECT * FROM Subscriptions WHERE sub_id = ? AND mag_id = ? AND expiration_date = ?", [sub_id, mag_id, expiration_date])
            results = cursor.fetchall()
            if len(results) > 0:
                print(f"Subscription already exists for {name}, {address}, {magazine_name}.")
                return
            
            #if subscription doesn't already exist, add data to table
            else:
                cursor.execute("INSERT INTO Subscriptions (sub_id, mag_id, expiration_date) VALUES (?, ?, ?)", [sub_id, mag_id, expiration_date])
        except sqlite3.Error as e:
            print(f"(A SQL error occured: {e})")
    

    #insert data into tables
    with sqlite3.connect('../db/magazines.db') as conn:
        conn.execute('PRAGMA foreign_keys = 1')
        cursor = conn.cursor()

        add_publisher(cursor, 'CTD Enterprises')
        add_publisher(cursor, 'Clobberdashers')
        add_publisher(cursor, 'Society of Silly Walks')

        add_magazine(cursor, 'CTD Awards', 'CTD Enterprises')
        add_magazine(cursor, 'CTD Today', 'CTD Enterprises')
        add_magazine(cursor, 'Clobber On', 'Clobberdashers')
        add_magazine(cursor, 'Clobb the Ladder to Success', 'Clobberdashers')
        add_magazine(cursor, 'Silly Tilly Walks on the Moon', 'Society of Silly Walks')
        add_magazine(cursor, 'Blah Blah Blah', 'Boo Hoo')

        add_subscriber(cursor, 'Ralph', '865 Leaf Lane')
        add_subscriber(cursor, 'Luis', '9 Rough Road')
        add_subscriber(cursor, 'Marianne', '12 Wild Way')
        add_subscriber(cursor, 'Marianne', '12 Wild Way')

        #subscribe(cursor, name, address, magazine_name, publisher_name, expiration_date)
        subscribe(cursor, 'Ralph', '865 Leaf Lane', 'CTD Awards', 'January 3, 2026')
        subscribe(cursor, 'Ralph', '865 Leaf Lane', 'CTD Today', 'February 8, 2026')
        subscribe(cursor, 'Luis', '9 Rough Road', 'CTD Awards', 'December 10, 2027')
        subscribe(cursor, 'Marianne', '12 Wild Way', 'Clobber On', 'March 30, 2026')
        subscribe(cursor, 'Marianne', '12 Wild Way', 'Clobb the Ladder to Success', 'March 30, 2026')
        subscribe(cursor, 'Marianne', '12 Wild Way', 'Silly Tilly Walks on the Moon', 'June 19, 2026')
        subscribe(cursor, 'Lily', '12 Wild Way', 'Clobber On', 'March 30, 2026')
        subscribe(cursor, 'Luis', '9 Rough Road', 'Hello There', 'December 9, 2025')

        conn.commit()

        print('Data inserted successfully.')


# **Task 4: Write SQL Queries**

# Write a query to retrieve all information from the subscribers table.
with sqlite3.connect('../db/magazines.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Subscribers')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Write a query to retrieve all magazines sorted by name.
with sqlite3.connect('../db/magazines.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Magazines ORDER BY mag_name')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Write a query to find magazines for a particular publisher, one of the publishers you created.  This requires a `JOIN`.
with sqlite3.connect('../db/magazines.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT Publishers.pub_name, Magazines.mag_name FROM Publishers INNER JOIN Magazines ON Publishers.pub_id = Magazines.pub_id WHERE Publishers.pub_name = "Clobberdashers"')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
