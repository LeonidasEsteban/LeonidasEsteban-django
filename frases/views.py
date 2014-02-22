from django.shortcuts import render
from frases.models import Frase

# Create your views here.
def home(req):

    frases = Frase.objects.all()
    return render(req, 'frases.html', {'frases':frases})
