from django.shortcuts import render
import pyrebase
import datetime
from django.http import JsonResponse
from django.http import HttpResponse
import threading
from django.http.response import StreamingHttpResponse
import json
import time

def movePassengersToTrain():
    #time.sleep(60)
    db = connectToDB()

    station = getStationCapacity(db) # number of person in the station
    train = getTrainCapacity(db)
    maxTrainCapacity = 10
    currentPassTrain = 0

    print("stationCapacity: " + str(maxTrainCapacity - station))
    print("trainCapacity: "  + str(train + station))

    if(station > maxTrainCapacity):
        setStationCapacity(db, str(maxTrainCapacity - station))
    else:
        setStationCapacity(db, str(station - maxTrainCapacity))
    
    setTrainCapacity(db, str(train + station))


def setTrainCapacity(db, value):
    #values
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    trainID = "1234"

    print("train value: " + value)

    #retrieves data
    data = db.child(date).child("trainCap").child(trainID).update({"capacity": int(value)})

def setStationCapacity(db, value):
    #values
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    stationID = "0"
    stationName = "Baclaran"

    print("station value: " + value)

    #retrieves data
    data = db.child(date).child("stationCap").child(stationID + " - " + stationName).update({"capacity": int(value)})

def connectToDB():
    config = {
        "apiKey": "AIzaSyAzsi129C620u9YU152wn-JudwKYn_8xyI",
        "authDomain": "puv-prediction-of-user-volume.firebaseapp.com",
        "databaseURL": "https://puv-prediction-of-user-volume.firebaseio.com",
        "projectId": "puv-prediction-of-user-volume",
        "storageBucket": "puv-prediction-of-user-volume.appspot.com",
        "messagingSenderId": "149609366284"
    };

    firebase = pyrebase.initialize_app(config)

    return firebase.database()

def retrieveData(db):
    #values
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    station = "0 - Baclaran"
    time = "13:45 - 13:59"

    #retrieves data
    data = db.child("2018-07-12").child("Entry").child(station).child(time).child("users").get()
    print(dict(data.val()))

    return dict(data.val())
    #print("Data: " +  str(data.val()))

def getStationCapacity(db):
    #values
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    stationID = "0"
    stationName = "Baclaran"

    #retrieves data
    data = db.child(date).child("stationCap").child(stationID + " - " + stationName).child("capacity").get()
    return int(data.val())

def getTrainCapacity(db):
    #values
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    trainID = "1234"

    #retrieves data
    data = db.child(date).child("trainCap").child(trainID).child("capacity").get()

    return int(data.val())

def retrieveAllData(db):
    #values
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    #retrieves data
    data = db.child(date).get()
    #print(dict(data.val()))

    return dict(data.val())

def stream_handler(message):
    #print(message["event"]) # put
    #print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    #print("asdf " + str(message["data"])) # {'title': 'Pyrebase', "body": "etc..."}
    jsonData = message["data"]
    #print(str(message["data"]))

db = connectToDB()

def getJSONData(request):
    data = retrieveData(db)

    #date = datetime.datetime.today().strftime('%Y-%m-%d')
    #my_stream = db.child(datetime).stream(dataListener)
    #print(type(my_stream))

    return HttpResponse(str(data), content_type="text/event-stream")

def getLiveJSONData(request):
    data = retrieveAllData(db)

    return HttpResponse(str(data), content_type="text/event-stream")

def sse(request):
    def itero():
        s = """retry: 2000\n\nevent: message\ndata: gg\n\n"""
        # data = json.dumps({'time':str(datetime.now())})
        data = retrieveAllData(db)
        s = '\n'.join(['retry: 1000', '\n', 'event: message', 'data: %s' % data, '\n'])
        yield s

        for i in range(10):
            s = '\n'.join(['retry: 1000', '\n', 'event: message', 'data: %s' % i, '\n'])
        for i in range(10):
            s = '\n'.join(['retry: 100000', '\n', 'event: message', 'data: %s' % i, '\n'])

        
        s = 'data:\n\n'
        s = ':\n\n'


    
    if request.META.get('HTTP_ACCEPT') == 'text/event-stream':
        response = StreamingHttpResponse(itero(), content_type="text/event-stream")
    else:
        response = HttpResponse(itero(), content_type="text/event-stream") 
    return   response

def home(request):

    context = [('BACLARAN', 'light'), ('EDSA', 'heavy'), ('LIBERTAD', 'light'), ('GIL-PUYAT', 'moderate'), ('VITO-CRUZ', 'light'), ('QUIRINO', 'light'), ('PEDRO-GIL', 'heavy'), ('UN-AVENUE', 'moderate'), ('CENTRAL-TERMINAL', 'light'),
    ('CARRIEDO', 'light'), ('DOROTEO-JOSE', 'heavy'), ('BAMBANG', 'moderate'), ('TAYUMAN', 'light'), ('BLUMENTRITT', 'light'), ('ABAD-SANTOS', 'moderate'), ('R-PAPA', 'heavy'), ('5TH-AVENUE', 'heavy'), ('MONUMENTO', 'light'),
    ('MALVAR', 'moderate'), ('BALINTAWAK', 'moderate'), ('ROOSEVELT', 'light')]

    context.reverse()

    currentStation = 'CARRIEDO'

    #threading.Thread(target=loop1_10).start()

    targetNumOfCurrentStation = getNumberOfStation(currentStation, context)

    movePassengersToTrain()

    return render(request, 'puv/index.html', {'data' : context, 'currentStation' : currentStation, 'numOfCurrentStation' : targetNumOfCurrentStation})

def getNumberOfStation(currentStation, context):

    targetNumOfCurrentStation = 1

    for i in context:
        if i[0] == currentStation:
            break
        else:
            targetNumOfCurrentStation = targetNumOfCurrentStation + 1

    return targetNumOfCurrentStation
