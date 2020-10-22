import aiosqlite
from aiosqlite import Error

async def create():
    try:
        conn = await aiosqlite.connect("data.db")
        conn.execute('''CREATE TABLE Blacklist
         (ID INT PRIMARY KEY     NOT NULL);''')
        conn.execute('''CREATE TABLE User_Messages
        (ID INT PRIMARY KEY     NOT NULL, MESSAGE           TEXT    NOT NULL);''')
        conn.execute('''CREATE TABLE UserInputMode
        (ID INT PRIMARY KEY     NOT NULL, OnOff           BIT    NOT NULL);''')
        conn.execute('''CREATE TABLE Catogory
        (ID INT PRIMARY KEY     NOT NULL, Catogory           INT    NOT NULL);''')
        conn.execute('''CREATE TABLE Datetime
        (ID INT PRIMARY KEY     NOT NULL, Datetime           INT    NOT NULL);''')
        await conn.commit()
    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()

def update(Table, VALUES):
    return
    
def read():
    return

def remove():
    return