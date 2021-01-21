import AsyncDataBase
async def reset(user):
    try:
        await AsyncDataBase.remove("Category", user.id)
    except:
        print("Error with removing from Category reset.py")
    try:    
        await AsyncDataBase.remove("User_Messages", user.id)
    except:
        print("Error with removing from User_Messages reset.py")