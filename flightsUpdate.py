import requests, json, pymongo

def flightsUpdateFunc(origin, destination, departureDate) :
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.testdb
    users_ticket = db.metaData
    users_key = db.keyData

    key = users_key.find_one({'key_id': {'$exists': True}})
    key_id=key.get('key_id')
    key_secret=key.get('key_pw')
    
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = "grant_type=client_credentials&client_id="+key_id+"&client_secret="+key_secret
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    res = requests.post(url, data=data, headers=headers)
    access_token = res.json().get('access_token')

    url = "https://test.api.amadeus.com/v1/shopping/flight-offers?origin="+origin+"&destination="+destination+"&departureDate="+departureDate+"&max=50&currency=KRW"
    headers = {"Authorization": "Bearer " + access_token}
    
    carriers = []
    locations = []

    datalist = requests.get(url, headers=headers)

    if datalist.status_code!=200:
        return [carriers,locations]

    datajson=datalist.json()
    data22 = datajson.get("data")

    for i in range(0, len(data22)):
        data22[i]["offerItems"][0]["price"]["totalTaxes"] = float(data22[i]["offerItems"][0]["price"]["totalTaxes"])
        data22[i]["offerItems"][0]["price"]["total"] = float(data22[i]["offerItems"][0]["price"]["total"])
        
    for key in range(0,len(data22)):
        users_ticket.insert(data22[key])

    data22 = datajson.get("dictionaries")

    for key in data22.keys() :
        if key=="carriers" :
            carriers=data22.get(key)
        elif key=="locations" :
            locations=data22.get(key)
    
    return [carriers, locations]
