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
        form = RequestForm.parse_obj(request.GET.dict())
    except ValueError as e:
        error_msg = e.errors()[0]["msg"]
        return JsonResponse({'error': str(error_msg)}, status=HTTPStatus.BAD_REQUEST)
    
    bees = Bees(
        request_url=form.url,
        request_method=form.method,
        request_body=form.body.decode("utf-8") if form.body else None,
        request_headers=json.dumps(dict(form.headers)) if form.headers else None
    )

    try:
        with transaction.atomic():
            response = requests.request(
                method=form.method,
                url=form.url,
                data=form.body,
            )
            response.raise_for_status()

            bees.response_code = response.status_code
            bees.response_content = response.content.decode('utf-8')
            bees.response_elapsed = response.elapsed.total_seconds()
            bees.save()
    except requests.exceptions.HTTPError as e:
        bees.response_code = e.response.status_code
        bees.response_content = e.response.content.decode('utf-8')
        bees.response_elapsed = e.response.elapsed.total_seconds()
        bees.save()

        return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    except requests.exceptions.RequestException as e:
        bees.save()

        return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    return JsonResponse(response.json(), status=HTTPStatus.OK, safe=False)


@require_GET
def bees_manager(request):
    num_bees = Bees.objects.count()
    return JsonResponse({"bees": num_bees}, status=HTTPStatus.OK)
