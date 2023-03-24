import json
from http import HTTPStatus

import requests
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .forms import RequestForm
from .models import Bees


@require_GET
def request_manager(request):
    try:
        params = request.GET.dict()
        params["body"] = json.loads(params["body"]) if params["body"] else None
        params["accept"] = params["accept"] if params["accept"] else None
        form = RequestForm.parse_obj(params)
    except ValueError as e:
        error_msg = e.errors()[0]["msg"]
        return JsonResponse({'error': str(error_msg)}, status=HTTPStatus.BAD_REQUEST)
    
    bees = Bees(
        request_url=form.url,
        request_method=form.method,
        request_body=form.body,
        request_headers=dict(request.headers),
        request_accept=form.accept
    )
    headers = {}
    if params["accept"]:
        headers = {"Accept": params["accept"]}
    try:
        response = requests.request(
            method=form.method,
            url=form.url,
            data=form.body,
            headers=headers
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    bees.response_code = response.status_code
    bees.response_content = response.content.decode('utf-8')
    bees.response_elapsed = response.elapsed.total_seconds()
    bees.save()
    return JsonResponse(response.json(), status=HTTPStatus.OK, safe=False)


@require_GET
def bees_manager(request):
    num_bees = Bees.objects.count()
    return JsonResponse({"bees": num_bees}, status=HTTPStatus.OK)
