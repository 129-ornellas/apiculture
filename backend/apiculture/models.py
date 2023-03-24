from django.db import models


class Bees(models.Model):
    request_url = models.CharField(max_length=2083)
    request_accept = models.CharField(max_length=256)
    request_method = models.CharField(max_length=6)
    request_body = models.JSONField(blank=True, null=True)
    request_headers = models.JSONField(blank=True, null=True)
    response_code = models.PositiveIntegerField()
    response_content = models.TextField(blank=True, null=True)
    response_elapsed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request_url
