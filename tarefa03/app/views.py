from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def usuarios(request):
    lista_usuarios = [
        {"nome": "Douglas", "matricula": 20221181110026, "idade": 18 , "cidade": "São Tomé"},
        {"nome": "Stephanny", "matricula": 20221181110040, "idade": 19 , "cidade": "São Tomé"},
        {"nome": "Paula", "matricula": 20221181110003, "idade": 19 , "cidade": "Sitio Novo"},
        {"nome": "Fernanda", "matricula": 20221181110030, "idade": 20 , "cidade": "Barcelona"},
        {"nome": "gaby", "matricula": 20221181110018, "idade": 21 , "cidade": "São Paulo do Potengi"},
    ]
    context = {
        "usuarios": lista_usuarios,
    }
    return render(request, "usuarios.html", context)