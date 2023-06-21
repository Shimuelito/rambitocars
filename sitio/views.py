from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sitio/index.html')

def catalogo(request):
    return render(request, 'sitio/catalogo.html')

def comentarios(request):
    return render(request, 'sitio/comentarios.html')

def contacto(request):
    return render(request, 'sitio/contacto.html')


def compra_supra(request):
    return render(request, 'sitio/compra/compra_supra.html')

def compra_subaru(request):
    return render(request, 'sitio/compra/compra_subaru.html')

def compra_nissan(request):
    return render(request, 'sitio/compra/compra_nissan.html')

def compra_350z(request):
    return render(request, 'sitio/compra/compra_350z.html')

def metodo_pago(request):
    return render(request, 'sitio/compra/metodo_pago.html')

def compra_realizada(request):
    return render(request, 'sitio/compra/compra_realizada.html')

def loginadmin(request):
    return render(request, 'sitio/admin/loginadmin.html')

def baseadmin(request):
    return render(request, 'sitio/admin/baseadmin.html')

def registroadmin(request):
    return render(request, 'sitio/admin/registroadmin.html')

def contraseñaadmin(request):
    return render(request, 'sitio/admin/contraseñaadmin.html')

def productoadmin(request):
    return render(request, 'sitio/admin/productoadmin.html')

def clienteadmin(request):
    return render(request, 'sitio/admin/clienteadmin.html')

def pedidosadmin(request):
    return render(request, 'sitio/admin/pedidosadmin.html')

def login(request):
    return render(request, 'sitio/usuario/login.html')

def registro(request):
    return render(request, 'sitio/usuario/registro.html')
