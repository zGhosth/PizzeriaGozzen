from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu import views
from menu.views import LocalViewSet  


router = DefaultRouter()
router.register(r'locales', LocalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('menu/', views.menu, name='menu'),
    path('iniciar_sesion/', views.iniciar_sesion, name='login'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('mapa/', views.mapa_local, name='mapa'),
    path('api/', include(router.urls)),
    path('crear_checkout/', views.crear_checkout, name='crear_checkout'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
