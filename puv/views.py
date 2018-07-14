from django.shortcuts import render
import pyrebase
import datetime
import collections
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

def getGraph(request):
    db = connectToDB()



    #retrieves data
    d1ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("9:15 - 9:29").child("users").get()
    data1 = dict(d1ata.val())
    d2ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("10:15 - 10:29").child("users").get()
    data2 = dict(d2ata.val())
    d3ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("11:15 - 11:29").child("users").get()
    data3 = dict(d3ata.val())
    d4ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("12:15 - 12:29").child("users").get()
    data4 = dict(d4ata.val())
    d5ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("13:15 - 13:29").child("users").get()
    data5 = {}
    d6ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("14:15 - 14:29").child("users").get()
    data6 = dict(d6ata.val())
    d7ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("15:15 - 15:29").child("users").get()
    data7 = dict(d7ata.val())
    d8ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("16:15 - 16:29").child("users").get()
    data8 = dict(d8ata.val())
    d9ata = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("17:15 - 17:29").child("users").get()
    data9 = dict(d9ata.val())

    print(data2)
    return render(request, 'puv/graph.html', {'jsonDAT1':len(data1), 'jsonDAT2':len(data2), 'jsonDAT3':len(data3), 'jsonDAT4':len(data4)
        , 'jsonDAT5':len(data5), 'jsonDAT6':len(data6), 'jsonDAT7':len(data7), 'jsonDAT8':len(data8), 'jsonDAT9':len(data9)})




#db = connectToDB()


    #retrieves data
#data = db.child("2018-07-12").child("Entry").child("0 - Baclaran").child("13:45 - 13:59").child("users").get()
#data2 = dict(data.val())
#print(data2)
#return render(request, 'puv/graph.html', {'jsonDATA':len(data2)})
