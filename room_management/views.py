from django.shortcuts import render

# Create your views here.
def start(request):

    return render(request, 'home.html')

def exit_ok(request):
    return render(request, 'exit_ok.html')

def home(request):
    params = {"room": "b302"}
    return render(request, 'home.html', context=params)

def exit_ok(request):
    return render(request, 'exit_ok.html')

def exit_confirmation(request):
    params = {"room": "b302"}
    return render(request, 'exit_confirmation.html', context=params)

def logout_ok(request):
    return render(request, 'logout_ok.html')

def in_confirmation(request):
    return render(request, 'in_confirmation.html')

def in_ok(request):
    params = {"room": "b302"}
    return render(request, 'in_ok.html', context=params)

def qr_reading(request):
    return render(request, 'qr_reading.html')