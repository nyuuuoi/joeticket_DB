import pymongo
def carrLocaInsertF(carriers, locations) :
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.testdb
    users_dict = db.dict
    
    users_dict.drop()
    
    users_dict.insert({'carriers':carriers})
    users_dict.insert({'locations':locations})
