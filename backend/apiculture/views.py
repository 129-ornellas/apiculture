from http import HTTPStatus

import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .forms import RequestForm


@require_http_methods(["GET"])
def request_manager(request):
    try:
        form = RequestForm.parse_obj(request.GET.dict())
    except ValueError as e:
        error_msg = e.errors()[0]["msg"]
        return JsonResponse({'error': str(error_msg)}, status=HTTPStatus.BAD_REQUEST)
    
    try:
        response = requests.request(
            method=form.method,
            url=form.url,
            data=form.data,
            headers=form.headers,
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    return JsonResponse(response.json(), status=HTTPStatus.OK, safe=False)
