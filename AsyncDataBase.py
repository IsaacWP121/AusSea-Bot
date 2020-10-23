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

async def update(Table, Values):
    try:
        _ = ""
        for x in Values:
            if _ == "":
                if isinstance(x, str):
                    _ = "'{}'".format(x)
                else:
                    _ = x
            else:
                if isinstance(x, str):
                    _ = "{}, '{}'".format(_, x)
                else:
                    _ = "{}, {}".format(_, x)
            Values = _
    except Error as e:
        print(e)
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        if Table == "Blacklist":
            await c.execute("INSERT INTO Blacklist (ID) VALUES ({})".format(Values))
        await conn.commit()
        print("data has been inputted into {}".format(Table))

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()
    
async def read(Table, ID):
    rd = None
    try:
        conn = await aiosqlite.connect("data.db")
        c = await conn.cursor()
        await c.execute("SELECT ID FROM {}".format(Table))
        rd = await c.fetchall()
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()
            if rd == None:
                return False
            else:
                return rd

def remove():
    return