from django.http import JsonResponse

def test_api(request):
    return JsonResponse({"mensaje": "Hola desde Django"})