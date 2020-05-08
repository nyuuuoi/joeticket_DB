import pymongo

def dbConvertFunc() :
  connection = pymongo.MongoClient("mongodb://localhost")
  db = connection.testdb
  users_test = db.metaData
  users_my = db.flightsData

  templist = users_test.find({},
                    {"_id":False,
                      "id":True,
                      "offerItems.services.segments.flightSegment.departure.iataCode": True,
                      "offerItems.services.segments.flightSegment.departure.at":True,
                      "offerItems.services.segments.flightSegment.arrival.iataCode":True,
                      "offerItems.services.segments.flightSegment.arrival.at":True,
                      "offerItems.services.segments.flightSegment.carrierCode":True,
                      "offerItems.services.segments.flightSegment.operating.carrierCode":True,
                      "offerItems.services.segments.flightSegment.duration":True,
                      "offerItems.price":True})
  
  users_my.drop()
  print("MyDB drop completed!")

  users_my.insert_many(templist)
  print("MyDB new data insert completed!")
