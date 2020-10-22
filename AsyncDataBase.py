import aiosqlite
from aiosqlite import Error

async def create():
    try:
        conn = await aiosqlite.connect("data.db")
        c = conn.cursor()
        await c.execute('''CREATE TABLE Blacklist
         (ID INT);''')
        await c.execute('''CREATE TABLE User_Messages
        (ID INT, MESSAGE TEXT);''')
        await c.execute('''CREATE TABLE UserInputMode
        (ID INT, OnOff INT);''')
        await c.execute('''CREATE TABLE Catogory
        (ID INT, Catogory INT);''')
        await c.execute('''CREATE TABLE Datetime
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
        print(_)
    except Error as e:
        print(e)
    try:
        conn = await aiosqlite.connect("data.db")
        c = conn.cursor()
        
        c.execute("INSERT INTO {} VALUES ({})".format(Table, Values))
        await conn.commit()
        print("data has been inputted into Blacklist")

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()
    
async def read(Table, ID):
    try:
        conn = await aiosqlite.connect("data.db")
        c = conn.cursor()
        await c.execute("SELECT * FROM {} WHERE ID={}".format(Table, ID))
        print(c.fetchall())
        await conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn:
            await conn.close()

def remove():
    return