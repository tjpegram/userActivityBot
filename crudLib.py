import pymongo
#create a new entry
def addUser(username):
    data = {"username": username, "messCount": 0}
    db.activitybot.insert_one(data)

#Getters for database info
def getUsername(username):
    val = db.activitybot.find({"username": username})
    for record in val:
        return (record["username"])

def getMessCount(username):
    val = db.activitybot.find({"username": username})
    for record in val:
        return(record["messCount"])

#setters for database info

def setUsername(username, newName):
    db.activitybot.find_one_and_update({"username": username}, {"$set": {"username": newName}})

def setMessCount(username, messCount):
    db.activitybot.find_one_and_update({"username": username}, {"$set": {"messCount": messCount}})

#delete a record
def removeUser(username):
    query = db.activitybot.find({"username": username})
    for record in query:
        db.activitybot.delete_one(record)




db = pymongo.MongoClient().activitybot
