from django.shortcuts import render


def index(request):
    data = {
        'title': 'Грумер - Юлия Александровна'
    }
    return render(request, 'grum/index.html', data)

def about(request):
    return render(request, 'grum/about.html')


def contact(request):
    return render(request, 'grum/contact.html')

def poroda(request):
    return render(request, 'grum/poroda.html')





