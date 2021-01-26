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
        (ID INT, OnOff BLOB);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS Category
        (ID INT, Category INT);''')
        await conn.commit()
    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()

async def addEntry(Table, ID, Message=None, BOOL=None, CAT=None):
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("INSERT INTO Blacklist (ID) VALUES (?)", (ID,))
        if Table == "User_Messages":
            await c.execute("INSERT INTO User_Messages(ID, MESSAGE) VALUES(?, ?)", (ID, Message))
        if Table == "UserInputMode":
            await c.execute("INSERT INTO UserInputMode(ID, OnOff) VALUES(?, ?)", (ID, BOOL))
        if Table == "Category":
            await c.execute("INSERT INTO Category(ID, Category) VALUES(?, ?)", (ID, CAT))
        print("data has been inputted into {}".format(Table))
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()

async def readall(Table):
    rd = None
    
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("SELECT * FROM Blacklist")
        if Table == "User_Messages":
            await c.execute("SELECT * FROM User_Messages")
        if Table == "UserInputMode":
            await c.execute("SELECT * FROM UserInputMode")
        rd = await c.fetchall()
        await conn.commit()


    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()
            if rd == None or rd == [] or rd == "":
                return False
            else:
                return rd

async def read(Table, ID):
    rd = None
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("SELECT * FROM Blacklist WHERE ID=?", (ID,))
        if Table == "User_Messages":
            await c.execute("SELECT * FROM User_Messages WHERE ID=?", (ID,))
        if Table == "UserInputMode":
            await c.execute("SELECT * FROM UserInputMode WHERE ID=?", (ID,))
        if Table == "Category":
            await c.execute("SELECT * FROM Category WHERE ID=?", (ID,))
        rd = await c.fetchall()
        await conn.commit()
        

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()
            if rd == None or rd == [] or rd == "":
                return False
            else:
                return rd
#Values is equal to message and id
async def update(Table, ID, Message=None, BOOL=None):
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "User_Messages":
            await c.execute('''UPDATE User_Messages SET MESSAGE = ? WHERE ID = ?''', (Message, ID))
        if Table == "UserInputMode":
            await c.execute('''UPDATE UserInputMode SET OnOff = ? WHERE ID = ?''', (BOOL, ID))
        await conn.commit()
    except Error as e:
        print(e)
    
    finally:
        if conn:
            await conn.close()

async def remove(Table, ID):
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "User_Messages":
            await c.execute("DELETE FROM User_Messages WHERE ID = ?", (ID,))
        if Table == "Blacklist":
            await c.execute("DELETE FROM Blacklist WHERE ID = ?", (ID,))
        if Table == "UserInputMode":
            await c.execute("DELETE FROM UserInputMode WHERE ID = ?", (ID,))
        if Table == "Category":
            await c.execute("DELETE FROM Category WHERE ID = ?", (ID,))
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()