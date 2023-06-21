from django.urls import path
from .views import index, catalogo,comentarios,contacto,compra_supra,compra_subaru,compra_nissan,compra_350z,metodo_pago,compra_realizada,loginadmin
from .views import baseadmin,registroadmin, contraseñaadmin,productoadmin, clienteadmin,pedidosadmin,login,registro
urlpatterns = [
    path('', index, name="index"),
    path('catalogo/', catalogo, name="catalogo"),
    path('comentarios/', comentarios, name="comentarios"),
    path('contacto/', contacto, name="contacto"),
    path('compra_supra/',compra_supra,name="compra_supra"),
    path('compra_subaru/',compra_subaru, name="compra_subaru"),
    path('compra_nissan/', compra_nissan, name="compra_nissan"),
    path('compra_350z/', compra_350z, name="compra_350z"),
    path('metodo_pago/', metodo_pago,name="metodo_pago"),
    path('compra_realizada/', compra_realizada,name="compra_realizada"),
    path('loginadmin/', loginadmin, name="loginadmin"),
    path('baseadmin/',baseadmin, name="baseadmin"),
    path('registroadmin/',registroadmin, name="registroadmin"),
    path('contraseñaadmin/', contraseñaadmin, name="contraseñaadmin"),
    path('productoadmin/', productoadmin, name="productoadmin"),
    path('clienteadmin/', clienteadmin, name="clienteadmin"),
    path('pedidosadmin/',pedidosadmin, name="pedidosadmin"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro",)
]