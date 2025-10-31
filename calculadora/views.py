from django.shortcuts import render
from .antlr.main import ejecutar_calculadora

def index(request):
    resultado = None
    codigo = None

    if request.method == "POST":
        codigo = request.POST.get("codigo", "")
        resultado = ejecutar_calculadora(codigo)

    return render(request, "calculadora/index.html", {
        "resultado": resultado,
        "codigo": codigo
    })
