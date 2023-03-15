from django.shortcuts import render

# Create your views here.
def index(request):

    info = {
        'name': 'jena',
        'age': 21,
    }

    return render(request, 'myapp/index.html', {'info': info})