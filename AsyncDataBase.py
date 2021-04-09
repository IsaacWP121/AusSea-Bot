import aiosqlite
from aiosqlite import Error

async def create():
    conn = await aiosqlite.connect("file::memory:?cache=shared")
    try:
        c = await conn.cursor()
        await c.execute('''CREATE TABLE IF NOT EXISTS Blacklist
         (ID INT);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS UserInputMode
        (ID INT, OnOff BLOB);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS selectionModMode
        (ID INT, OnOff BLOB);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS Category
        (ID INT, Category INT);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS ModCategory
        (ID INT, Category INT);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS mentorSelect
        (ID INT, Category BLOB, Status BOOL);''')
        await c.execute('''CREATE TABLE IF NOT EXISTS Offline (ID INT, Status BOOL);''')
        await conn.commit()
    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()


async def addEntry(Table, ID, Message=None, BOOL=None, CAT=None):
    conn = await aiosqlite.connect("file::memory:?cache=shared")
    try:
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("INSERT INTO Blacklist (ID) VALUES (?)", (ID,))
        if Table == "UserInputMode":
            await c.execute("INSERT INTO UserInputMode(ID, OnOff) VALUES(?, ?)", (ID, BOOL))
        if Table == "selectionModMode":
            await c.execute("INSERT INTO selectionModMode(ID, OnOff) VALUES(?, ?)", (ID, BOOL))
        if Table == "Category":
            await c.execute("INSERT INTO Category(ID, Category) VALUES(?, ?)", (ID, CAT))
        if Table == "ModCategory":
            await c.execute("INSERT INTO ModCategory(ID, Category) VALUES(?, ?)", (ID, CAT))
        if Table == "mentorSelect":
            await c.execute("INSERT INTO mentorSelect(ID, Category, Status) VALUES(?, ?, ?)", (ID, CAT, BOOL))
        if Table == "Offline":
            await c.execute("INSERT INTO Offline (ID, Status) VALUES (1, ?)", (BOOL,))
        print("data has been inputted into {}".format(Table))
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()


async def readall(Table):
    rd = None
    conn = await aiosqlite.connect("file::memory:?cache=shared")
    try:
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("SELECT * FROM Blacklist")
        if Table == "UserInputMode":
            await c.execute("SELECT * FROM UserInputMode")
        if Table == "selectionModMode":
            await c.execute("SELECT * FROM selectionModMode")
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


async def read(Table, ID, rv = 2):
    rd = None
    conn = await aiosqlite.connect("file::memory:?cache=shared")
    try: 
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("SELECT * FROM Blacklist WHERE ID=?", (ID,))
        if Table == "UserInputMode":
            await c.execute("SELECT * FROM UserInputMode WHERE ID=?", (ID,))
        if Table == "selectionModMode":
            await c.execute("SELECT * FROM selectionModMode WHERE ID=?", (ID,))
        if Table == "Category":
            await c.execute("SELECT * FROM Category WHERE ID=?", (ID,))
        if Table == "ModCategory":
            await c.execute("SELECT * FROM ModCategory WHERE ID=?", (ID,))
        if Table == "mentorSelect":
            await c.execute("SELECT * FROM mentorSelect WHERE ID=?", (ID,))
        if Table == "Offline":
            await c.execute("SELECT * FROM Offline WHERE ID=1")
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
                if Table == "mentorSelect":
                    return rd[0][rv]
                try:
                    return rd[0][1]
                except:
                    return rd[0][0]


async def update(Table, ID, CAT=None, BOOL=None):
    conn = await aiosqlite.connect("file::memory:?cache=shared")
    try:
        c = await conn.cursor()
        if Table == "UserInputMode":
            await c.execute('''UPDATE UserInputMode SET OnOff = ? WHERE ID = ?''', (BOOL, ID))
        if Table == "selectionModMode":
            await c.execute('''UPDATE selectionModMode SET OnOff = ? WHERE ID = ?''', (BOOL, ID))
        if Table == "mentorSelect":
            await c.execute('''UPDATE mentorSelect SET CAT = ? WHERE ID = ?''', (CAT, ID))
        if Table == "Offline":
            await c.execute('''UPDATE Offline SET Status = ? WHERE ID = 1''', (BOOL,))
        await conn.commit()
    except Error as e:
        print(e)
    
    finally:
        if conn:
            await conn.close()


async def removeall():
    conn = await aiosqlite.connect("file::memory:?cache=shared")
    try:
        c = await conn.cursor()
        await c.execute("DELETE FROM UserInputMode")
        await c.execute("DELETE FROM selectionModMode")
        await c.execute("DELETE FROM Category")
        await c.execute("DELETE FROM ModCategory")
        await c.execute("DELETE FROM mentorSelect")
        await c.execute("DELETE FROM Offline")
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()


async def remove(Table, ID):
    conn = await aiosqlite.connect("file::memory:?cache=shared")
    try:
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("DELETE FROM Blacklist WHERE ID = ?", (ID,))
        if Table == "UserInputMode":
            await c.execute("DELETE FROM UserInputMode WHERE ID = ?", (ID,))
        if Table == "selectionModMode":
            await c.execute("DELETE FROM selectionModMode WHERE ID = ?", (ID,))
        if Table == "Category":
            await c.execute("DELETE FROM Category WHERE ID = ?", (ID,))
        if Table == "ModCategory":
            await c.execute("DELETE FROM ModCategory WHERE ID = ?", (ID,))
        if Table == "mentorSelect":
            await c.execute("DELETE FROM mentorSelect WHERE ID = ?", (ID,))
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()