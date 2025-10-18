from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

# Create your views here.

# Listar clientes - CORREGIDO
def index(request):
    clientes = Cliente.objects.all()  # Cambié 'Cliente' por 'clientes'
    return render(request, 'listar_cliente.html', {'clientes': clientes})  # Cambié el nombre del template

# Ver cliente individual - CORREGIDO (esta es la función que falta)
def ver_cliente(request, cliente_id):  # ← CAMBIÉ el nombre de 'ver_juguetes' a 'ver_cliente'
    cliente = get_object_or_404(Cliente, id=cliente_id)  # ← CORREGIDO: usa 'cliente_id'
    return render(request, 'ver_cliente.html', {'cliente': cliente})

def agregar_cliente(request):
    if request.method == 'POST':
        # Recupera los datos del formulario POST
        apepaterno = request.POST.get('apepaterno')
        apematerno = request.POST.get('apematerno')
        nombre = request.POST.get('nombre')
        domicilio = request.POST.get('domicilio')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        alergias = request.POST.get('alergias')

        # Crea y guarda el nuevo cliente
        Cliente.objects.create(
            apepaterno=apepaterno,
            apematerno=apematerno,
            nombre=nombre,
            domicilio=domicilio,
            email=email,
            telefono=telefono,
            alergias=alergias
        )
        return redirect('inicio')  # ← Cambié a 'inicio' que es el nombre de tu URL principal
    return render(request, 'agregar_cliente.html')

# Editar cliente
def editar_cliente(request, id):  # ← El parámetro debe ser 'id' para coincidir con la URL
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        cliente.apepaterno = request.POST.get('apepaterno')
        cliente.apematerno = request.POST.get('apematerno')
        cliente.nombre = request.POST.get('nombre')
        cliente.domicilio = request.POST.get('domicilio')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.alergias = request.POST.get('alergias')
        cliente.save()
        return redirect('inicio')
    return render(request, 'editar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):  # ← El parámetro debe ser 'id' para coincidir con la URL
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('inicio')
    return render(request, 'borrar_cliente.html', {'cliente': cliente})