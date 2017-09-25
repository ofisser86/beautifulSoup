from django.shortcuts import render


def imbdparser(request):
    return render(request, 'imbd/index.html', {})

# Create your views here.
