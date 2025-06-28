from django.shortcuts import render
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Stripe: crear sesión de pago
@csrf_exempt
def crear_checkout(request):
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'clp',
                        'product_data': {
                            'name': 'Pedido Pizzería',
                        },
                        'unit_amount': 15000,  # En centavos CLP: $15000
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:8000/success/',
                cancel_url='http://localhost:8000/cancel/',
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Vistas normales
def inicio(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def ubicacion(request):
    return render(request, 'ubicacion.html')

def mapa_local(request):
    return render(request, 'mapa.html')

# Vistas para redirecciones de Stripe
def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

# API REST de Locales
from rest_framework import viewsets
from .models import Local
from .serializers import LocalSerializer

class LocalViewSet(viewsets.ReadOnlyModelViewSet):  # Solo lectura
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
