from http import HTTPStatus

import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .forms import RequestForm


@require_GET
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
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    return JsonResponse(response.json(), status=HTTPStatus.OK, safe=False)

@require_GET
def bees_manager(request):
    num_bees = Bees.objects.count()
    return JsonResponse({"bees": num_bees}, status=HTTPStatus.OK)