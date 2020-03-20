from django.http import HttpResponse
from django.http import HttpResponseNotFound
import operator
# Create your views here.


def index(request):
    return HttpResponse("Hola, mundo. Estás en la página de inicio de tu app llamada calc.")

operations = {
    "sumar": operator.add,
    "restar": operator.sub,
    "multiplicar": operator.mul,
    "dividir": operator.truediv
}

def calcular(request, func, op1, op2):
	if func not in operations:
	    return HttpResponseNotFound("Introduce una operacion: sumar, restar, multiplicar o dividir")
	try:
	    op1 =  float(op1)
	    op2 =  float(op2)
	except ValueError:
	    return HttpResponseNotFound("Introduce un operando valido tipo decimal")
	try:
	    result = operations[func](op1, op2)
	except ZeroDivisionError:
	    return HttpResponseNotFound("Para realizar una division el divisor debe ser distinto de 0")
	return HttpResponse("El resultado es: "+ str(result))
