from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SaludoView(APIView):
    def get(self, request):
        return Response({"message": "Hola, Mundo!"})
    

class SaludoPersonalizadoView(APIView):
    def post(self, request):
        nombre = request.data.get("nombre", "invitado")  # Valor por defecto si no se envía
        mensaje = f"Hola, {nombre}!"
        return Response({"mensaje": mensaje})