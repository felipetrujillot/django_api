from django.http import HttpResponse, JsonResponse


def api(request):
    """
    Función inicial de la API, para validar su correcto funcionamiento

    :param request: The HTTP request object.
    :return: A JSON response with the message 'ok' and the data 'api python'.
    """
    return JsonResponse({
        'msg': 'ok',
        'data': 'api python'
    })


def ejemplo(request, hola):
    """
    Función ejemplo

    :param request: The HTTP request object.
    :return: A JSON response with the message 'ok' and the data 'api python'.
    """
    return JsonResponse({
        'msg': 'ok',
        'data': 'test'
    })
