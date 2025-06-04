from django.shortcuts import render

# Create your views here.
#def tienda_negocio(request):
#   subdominio = request.get_host().split(".")[0]  # Extrae el subdominio
#    negocio = Negocio.objects.filter(subdominio=subdominio).first()
#    productos = Producto.objects.filter(negocio=negocio)
#    return render(request, "tienda.html", {"negocio": negocio, "productos": productos})