from django.shortcuts import render


def index(request):
    context = {
        'hello': 'Hello World!'
    }
    return render(request, 'polls/index.html', context)
