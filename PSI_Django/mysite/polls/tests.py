from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views, api
from .models import Dead_people, Nagrobki
from rest_framework import status
from django.utils.http import urlencode
from django import urls


class Dead_peopleTests(APITestCase):
    def post_Dead_people(self, Name):
        url = reverse(api.Dead_peopleList.name)
        data = {'Name': Name}
        response = self.client.post(url, data, format='json')
        return response

    def test_update_Dead_people(self):
        Dead_people_name = 'bol'
        response = self.post_Dead_people(Dead_people_name)
        url = urls.reverse(api.Dead_peopleDetail.name, None, {response.data['pk']})
        updated_Dead_people_name = 'New bol'
        data = {'name': updated_Dead_people_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_Dead_people_name

    def test_get_Dead_people(self):
        Dead_people_name = 'bol'
        response = self.post_Dead_people(Dead_people_name)
        url = urls.reverse(api.Dead_peopleDetail.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == Dead_people_name

class NagrobkiTests(APITestCase):
    def post_Nagrobki(self, Name):
        url = reverse(api.NagrobkiList.name)
        data = {'Name': Name}
        response = self.client.post(url, data, format='json')
        return response

    def test_update_Dead_people(self):
        Nagrobki_name = 'dol'
        response = self.post_Nagrobki(Nagrobki_name)
        url = urls.reverse(api.NagrobkiDetail.name, None, {response.data['pk']})
        updated_Nagrobki_name = 'New dol'
        data = {'name': updated_Nagrobki_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_Nagrobki_name

    def test_get_Dead_people(self):
        Nagrobki_name = 'dol'
        response = self.post_Nagrobki(Nagrobki_name)
        url = urls.reverse(api.Nagrobki.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == Nagrobki_name