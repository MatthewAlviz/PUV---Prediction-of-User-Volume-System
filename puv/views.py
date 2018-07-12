from django.shortcuts import render

def home(request):

    context = [('BACLARAN', 'light'), ('EDSA', 'heavy'), ('LIBERTAD', 'light'), ('GIL PUYAT', 'moderate'), ('VITO CRUZ', 'light'), ('QUIRINO', 'light'), ('PEDRO GIL', 'heavy'), ('UN AVENUE', 'moderate'), ('CENTRAL TERMINAL', 'light'),
    ('CARRIEDO', 'light'), ('DOROTEO JOSE', 'heavy'), ('BAMBANG', 'moderate'), ('TAYUMAN', 'light'), ('BLUMENTRITT', 'light'), ('ABAD SANTOS', 'moderate'), ('R.PAPA', 'heavy'), ('5TH AVENUE', 'heavy'), ('MONUMENTO', 'light'),
    ('MALVAR', 'moderate'), ('BALINTAWAK', 'moderate'), ('ROOSEVELT', 'light')]

    context.reverse()

    return render(request, 'puv/index.html', {'data' : context})
