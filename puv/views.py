from django.shortcuts import render
import pyrebase
import datetime
from django.http import JsonResponse
from django.http import HttpResponse

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

def dataListener(message):
    #print(message["event"]) # put
    #print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    #print("asdf " + str(message["data"])) # {'title': 'Pyrebase', "body": "etc..."}
    return message["data"]

jsonData = {}

def getJSONData(request):
    db = connectToDB()
    data = retrieveData(db)

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    my_stream = db.child(date).stream(dataListener) 

    return HttpResponse(str(data), content_type="text/event-stream")

def home(request):

    context = [('BACLARAN', 'light'), ('EDSA', 'heavy'), ('LIBERTAD', 'light'), ('GIL-PUYAT', 'moderate'), ('VITO-CRUZ', 'light'), ('QUIRINO', 'light'), ('PEDRO-GIL', 'heavy'), ('UN-AVENUE', 'moderate'), ('CENTRAL-TERMINAL', 'light'),
    ('CARRIEDO', 'light'), ('DOROTEO-JOSE', 'heavy'), ('BAMBANG', 'moderate'), ('TAYUMAN', 'light'), ('BLUMENTRITT', 'light'), ('ABAD-SANTOS', 'moderate'), ('R-PAPA', 'heavy'), ('5TH-AVENUE', 'heavy'), ('MONUMENTO', 'light'),
    ('MALVAR', 'moderate'), ('BALINTAWAK', 'moderate'), ('ROOSEVELT', 'light')]

    context.reverse()

    currentStation = 'CARRIEDO'

    targetNumOfCurrentStation = getNumberOfStation(currentStation, context)


    return render(request, 'puv/index.html', {'data' : context, 'currentStation' : currentStation, 'numOfCurrentStation' : targetNumOfCurrentStation})

def getNumberOfStation(currentStation, context):

    targetNumOfCurrentStation = 1

    for i in context:
        if i[0] == currentStation:
            break
        else:
            targetNumOfCurrentStation = targetNumOfCurrentStation + 1

    return targetNumOfCurrentStation
