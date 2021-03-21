import AsyncDataBase
async def reset(user):
    try:
        await AsyncDataBase.remove("Category", user.id)
    except:
        print("Error with removing from Category reset.py")
    try:    
        await AsyncDataBase.remove("ModCategory", user.id)
    except:
        print("Error removing from ModCategory reset.py")
    try:    
        await AsyncDataBase.remove("selectionModMode", user.id)
    except:
        print("Error removing from ModCategory reset.py")
    try:    
        await AsyncDataBase.remove("selectionModMode", user.id)
    except:
        print("Error with removing from UserInputMode reset.py")
