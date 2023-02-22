from http import HTTPStatus

import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .forms import GetForm


@require_http_methods(["GET"])
def get(request):
    try:
        form = GetForm.parse_obj(request.GET.dict())
    except ValueError as e:
        error_msg = e.errors()[0]["msg"]
        return JsonResponse({'error': str(error_msg)}, status=HTTPStatus.BAD_REQUEST)
    
    try:
        response = requests.get(form.url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    return JsonResponse(response.json(), status=HTTPStatus.OK, safe=False)

@require_http_methods(["POST"])
def post(request):
    return JsonResponse({"post": 200})

@require_http_methods(["PUT"])
def put(request):
    return JsonResponse({"put": 200})

@require_http_methods(["PATCH"])
def patch(request):
    return JsonResponse({"patch": 200})

@require_http_methods(["DELETE"])
def delete(request):
    return JsonResponse({"delete": 200})
