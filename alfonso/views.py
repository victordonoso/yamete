from datetime import datetime
from django.shortcuts import render

def primos():
    primos = []
    for num in range(1,101):
        primo = True
        for i in range(2,num):
            if (num%i==0):
                primo = False
        if primo:
            primos.append(num)
    return primos  

def hora():
    hora = datetime.now()
    saludo = 'Buenos días'
    if hora.hour < 12:
        saludo = 'Buenos días'
    elif hora.hour < 20:
        saludo = 'Buenas tardes'
    else:
        saludo = 'Buenas noches'
    return saludo

def numeros_primos(request):
    return render(request, 'numeros_primos.html', {
        'listado':primos(), 
        'hora':hora()})
