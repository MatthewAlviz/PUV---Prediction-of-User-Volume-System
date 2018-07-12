from django.shortcuts import render

def home(request):
    context = {"BACLARAN":"light", "EDSA":"heavy", "LIBERTAD":"light", "GIL PUYAT":"moderate", "VITO CRUZ":"light", "QUIRINO":"light", "PEDRO GIL":"heavy", "BACLARAN":"light", "UN AVENUE":"moderate", "CENTRAL TERMINAL":"light",
    "CARRIEDO":"light", "DOROTEO JOSE":"heavy", "BAMBANG":"moderate", "TAYUMAN":"light", "BLUMENTRITT":"light", "ABAD SANTOS":"moderate", "BACLARAN":"light", "R.PAPA":"heavy", "5TH AVENUE":"heavy", "MONUMENTO":"light", "MALVAR":"moderate", "BALINTAWAK":"moderate",
    "ROOSEVELT":"light"}

    return render(request, 'puv/index.html', {'data' : context})
