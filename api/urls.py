from django.urls import path
from .views import SaludoView
from .views import SaludoPersonalizadoView

urlpatterns = [
    path('saludo/', SaludoView.as_view(), name='saludo'),
    path('saludo-personalizado/', SaludoPersonalizadoView.as_view(),name='saludo_personalizado')
]