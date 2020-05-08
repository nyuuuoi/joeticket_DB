import pymongo


def delPastDate(deldate) :
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.testdb
    users_my = db.flightsData
    users_test = db.metaData
    
    x = users_my.delete_many({"offerItems.0.services.0.segments.0.flightSegment.departure.at":{'$regex':deldate}})
    print("MyDB ",x.deleted_count,"documents deleted")
    x = users_test.delete_many({"offerItems.0.services.0.segments.0.flightSegment.departure.at":{'$regex':deldate}})
    print("testdb ",x.deleted_count,"documents deleted")
