# import time, threading, datetime
from flightsDate import makeDateList
from call_update import dbUpdateFunc
from flightsConvert import dbConvertFunc

airportList = ['ICN','GMP','PUS', 'KIX', 'HKG', 'KBP', 'HEL']
carriers=[]
locations=[]

def thread_run():
    # print(datetime.datetime.now())
    #루틴 하나 시작시간 체크
    newdateList=makeDateList()
    
    dbUpdateFunc(airportList, newdateList)

    dbConvertFunc()
    
thread_run()
# def lambda_handler(event, context):
#     return thread_run()
