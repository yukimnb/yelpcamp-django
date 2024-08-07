from accounts.models import CustomUser
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="hogehoge",
        )

    # def test_campground_list_create_api_view(self):
    #     url = reverse("apiv1:campground-list-create")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_campground_retrieve_update_destroy_api_view(self):
    #     url = reverse("apiv1:campground-retrieve-update-destroy", args=[1])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_review_list_create_api_view(self):
    #     url = reverse("apiv1:review-list-create", args=[1])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_review_destroy_api_view(self):
    #     url = reverse("apiv1:review-destroy", args=[1])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_accounts_signup(self):
        url = reverse("apiv1:rest_register")
        response = self.client.post(
            url, {"email": "test@example.com", "password1": "testpassword", "password2": "testpassword"}
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_accounts_logout(self):
        url = reverse("apiv1:rest_logout")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accounts_login(self):
        url = reverse("apiv1:login")
        response = self.client.post(url, {"email": "testuser@example.com", "password": "hogehoge"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
