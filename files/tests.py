import os

from django.urls import reverse
from django.test import TestCase


class AircodeAPITests(TestCase):
    def test_upload(self):
        url = reverse("upload")
        with open('your/file/path/') as f:
            response = self.client.post(url, {'file': f}, format='multipart')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'ok')
