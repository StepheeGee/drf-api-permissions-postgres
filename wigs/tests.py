# wigs/tests.py
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Wig
from rest_framework.test import force_authenticate

def get_user(client):
    # Check if the user already exists
    existing_user = get_user_model().objects.filter(username="testuser").first()

    if existing_user:
        force_authenticate(client, user=existing_user)
        return existing_user

    # If the user doesn't exist, create a new one
    user = get_user_model().objects.create_user(
        username="testuser", password="pass"
    )
    force_authenticate(client, user=user)
    
    response = client.get('/api/v1/user/')
    return get_user_model().objects.get(id=response.data.get('id'))

class WigTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(
            username="testuser", password="pass"
        )
        testuser.save()

        test_wig = Wig.objects.create(
            name="Sample Wig",
            purchaser=testuser,
            color="Black",
            length=20.0,
            original_curl_pattern="curly",
            original_density=50,
            original_hair_origin="brazilian",
            description="A sample wig for testing.",
            price=100.0,
        )
        test_wig.save()

    def setUp(self):
        self.client.login(username="testuser", password="pass")

    def test_wig_model(self):
        wig = Wig.objects.get(id=1)
        actual_purchaser = str(wig.purchaser)
        actual_name = str(wig.name)
        actual_description = str(wig.description)
        self.assertEqual(actual_purchaser, "testuser")
        self.assertEqual(actual_name, "Sample Wig")
        self.assertEqual(actual_description, "A sample wig for testing.")

    def test_get_wig_list(self):
        url = reverse("wig-list")  # Adjust the URL based on your urlpatterns
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        wigs = response.data
        self.assertEqual(len(wigs), 1)
        self.assertEqual(wigs[0]["name"], "Sample Wig")

    def test_get_wig_by_id(self):
        url = reverse("wig-detail", args=(1,))  # Adjust the URL based on your urlpatterns
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        wig = response.data
        self.assertEqual(wig["name"], "Sample Wig")

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("wig-list")  # Adjust the URL based on your urlpatterns
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_wig(self):
        url = reverse("wig-list")
        data = {
            "name": "New Wig",
            "color": "Blonde",
            "length": 24.0,
            "original_curl_pattern": "straight",
            "original_density": 60,
            "original_hair_origin": "peruvian",
            "description": "A new wig for testing.",
            "price": 120.0,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        wigs = Wig.objects.all()
        self.assertEqual(len(wigs), 2)
        self.assertEqual(Wig.objects.get(id=2).name, "New Wig")

    def test_update_wig(self):
        url = reverse("wig-detail", args=(1,))
        data = {
            "name": "Updated Wig",
            "color": "Red",
            "length": 22.0,
            "original_curl_pattern": "curly",
            "original_density": 70,
            "original_hair_origin": "brazilian",
            "description": "An updated wig for testing.",
            "price": 150.0,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        wig = Wig.objects.get(id=1)
        self.assertEqual(wig.name, data["name"])
        self.assertEqual(wig.color, data["color"])
        # Add more assertions for other fields as needed

    def test_delete_wig(self):
        url = reverse("wig-detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        wigs = Wig.objects.all()
        self.assertEqual(len(wigs), 0)



    def test_switch_user(self):
        self.client.logout()
        user_to_switch = get_user(self.client)
        self.client.force_login(user_to_switch)  # Use force_login to authenticate the user

        url = reverse("wig-list")  # Adjust the URL based on your urlpatterns
        response = self.client.get(url)
        print(response.data)  # Add this line to print the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_user(self.client).username, "testuser") 


