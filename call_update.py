from flightsUpdate import flightsUpdateFunc
from carrLocaInsert import carrLocaInsertF
import pymongo
carriers = {}
locations = {}
def dbUpdateFunc(airportList, dateList) :
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.testdb
    users_ticket = db.metaData
    users_key = db.keyData
    users_ticket.drop()

    for dat in dateList:
        for dep in airportList:
            for arr in airportList:
                if(dep==arr or (dep=="ICN" and arr=="GMP") or (dep=="GMP" and arr=="ICN")) :
                    continue
                else :
                    tmpcarriers, tmplocations = flightsUpdateFunc(dep, arr, dat)
                    apicnt = users_key.find_one({'apicnt': {'$exists': True}})
                    if (2000-apicnt.get('apicnt')) < 40:
                       print("key만료")
                       users_key.delete_one({'key_id': {'$exists': True}})
                       users_key.update({'apicnt': {'$exists': True}}, {'$set': {'apicnt': 0}})
                    else :
                       users_key.update({'apicnt': {'$exists': True}},{'$inc':{'apicnt':1}})
                    carriers.update(tmpcarriers)
                    locations.update(tmplocations)
                    apicnt = users_key.find_one({'apicnt': {'$exists': True}})
                    print(dep,"------",arr,"------",dat,"------완뇨!!  apicnt = ",apicnt.get('apicnt'))
    carrLocaInsertF(carriers, locations)
