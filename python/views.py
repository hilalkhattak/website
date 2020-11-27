from django.shortcuts import render




def home(request):
    return render(request, 'python.html')

def code(request):
    return render(request, 'stepsintopython.html')

def expressions(request):
    return render(request, 'expressions.html')

def variables(request):
    return render(request, 'variables.html')

def io(request):
    return render(request, 'io.html')

def functions(request):
    return render(request, 'functions.html')



