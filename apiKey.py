import pymongo

#TimerNew.py실행 전에 먼저 최초 1회 실행 필요
def apiKeyFunc() :
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.testdb
    users_key = db.keyData

    keyList = [['Z57ZzeIpKnVCOiJ6dz0EwmyQnlYLy8TG', '8jxJ4IvTCsxIp5mj'],
               ['O9XxtiDuOHqPXXN33AVtMkA4Wefo490D', 'v4fC9g4nsbyZDA0F'],
               ['WTGHNN0y29dXOsO1pqczox3tzcTWGaQ3', 'iyDoJy0v2y2Zq4Ic'],
               ['Jj6ogTnHlEw4QvzJr7RFAc39ouD7RSWz', 'WBMwA3QQpVZaM5mX']]

    users_key.insert({'apicnt': 2077})

    for i in range(0, len(keyList)):
        print(keyList[i][0], keyList[i][1])
        users_key.insert({'key_id':keyList[i][0],'key_pw':keyList[i][1]})
           
apiKeyFunc()
