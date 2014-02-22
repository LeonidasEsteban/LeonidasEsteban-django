from django.shortcuts import render
from frases.models import Frase

# Create your views here.
def home(req):

    frases = Frase.objects.all()[:1]
    return render(req, 'home.html', {'frases':frases})
