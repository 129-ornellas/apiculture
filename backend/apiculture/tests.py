import json
from http import HTTPStatus

from django.urls import reverse


def test_bees_manager(client, db):
    url = reverse("bees_manager")
    response = client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert "bees" in json.loads(response.content)
