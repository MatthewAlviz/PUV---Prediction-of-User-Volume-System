from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

global userStationChoice

def homeview(request): # TRAIN DISPLAY
    context = [('BACLARAN', 'light'), ('EDSA', 'heavy'), ('LIBERTAD', 'light'), ('GIL-PUYAT', 'moderate'), ('VITO-CRUZ', 'light'), ('QUIRINO', 'light'), ('PEDRO-GIL', 'heavy'), ('UN-AVENUE', 'moderate'), ('CENTRAL-TERMINAL', 'light'),
    ('CARRIEDO', 'light'), ('DOROTEO-JOSE', 'heavy'), ('BAMBANG', 'moderate'), ('TAYUMAN', 'light'), ('BLUMENTRITT', 'light'), ('ABAD-SANTOS', 'moderate'), ('R-PAPA', 'heavy'), ('5TH-AVENUE', 'heavy'), ('MONUMENTO', 'light'),
    ('MALVAR', 'moderate'), ('BALINTAWAK', 'moderate'), ('ROOSEVELT', 'light')]

    context.reverse()

    currentStation = 'BACLARAN'

    targetNumOfCurrentStation = getNumberOfStation(currentStation, context)


    return render(request, 'puv/index.html', {'data' : context, 'currentStation' : currentStation, 'numOfCurrentStation' : targetNumOfCurrentStation})

def userview(request): # USER DISPLAY
    return render(request, 'puv/userview.html')

def getNumberOfStation(currentStation, context):

    targetNumOfCurrentStation = 1

    for i in context:
        if i[0] == currentStation:
            break
        else:
            targetNumOfCurrentStation = targetNumOfCurrentStation + 1

    return targetNumOfCurrentStation

def userview2(request):
    global userStationChoice
    stationVal = userStationChoice
    return render(request, 'puv/userview2.html', {'station': stationVal})

def storePickedStation(request):
    if request.method == 'POST':

        global userStationChoice
        userStationChoice = request.POST['user']

        data = {
            'status': 'success'
        }

    return JsonResponse(data)
