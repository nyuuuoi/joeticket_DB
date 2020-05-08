import datetime

def makeDateList() :
    #조회가능한 기간 리스트(datelist) 자동화
    x=datetime.datetime.now()
    datelist = []
    for i in range(0,1) :
        y=x+datetime.timedelta(+i)
        datelist.append(str(y.date()))
    return datelist
