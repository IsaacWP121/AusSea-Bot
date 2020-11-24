import aiosqlite
from aiosqlite import Error

async def create():
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        await c.execute('''CREATE TABLE IF NOT EXISTS Blacklist
         (ID INT);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS User_Messages
        (ID INT, MESSAGE TEXT);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS UserInputMode
        (ID INT, OnOff INT);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS Catogory
        (ID INT, Catogory INT);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS Datetime
        (ID INT, Datetime INT);''')
        await conn.commit()
    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()

async def addEntry(Table, ID, Message=None):
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("INSERT INTO Blacklist (ID) VALUES ($1)", (ID))
        if Table == "User_Messages":
            print(await c.execute("INSERT INTO User_Messages(ID, MESSAGE) VALUES(?, ?)", (ID, Message)))
        print("data has been inputted into {}".format(Table))
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()
    
async def read(Table, ID):
    rd = None
    conn = await aiosqlite.connect("data.db")
    c = await conn.cursor()
    try:
        if Table == "Blacklist":
            await c.execute("SELECT * FROM Blacklist WHERE ID=?", [ID])
        if Table == "User_Messages":
            await c.execute("SELECT * FROM User_Messages WHERE ID=469067687616839691")

        rd = await c.fetchall()
        print(rd)
        await conn.commit()


    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()
            if rd == None or rd == []:
                return False
            else:
                return rd
#Values is equal to message and id
async def update(Table, Values):
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "User_Messages":
            await c.executemany('''UPDATE User_Messages SET MESSAGE = ? WHERE ID = ?''', Values)
        await conn.commit()
    except Error as e:
        print(e)
    
    finally:
        if conn:
            await conn.close()

async def remove(table, id):
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        await c.execute("DELETE FROM {} WHERE ID = {}".format(table, id))
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()