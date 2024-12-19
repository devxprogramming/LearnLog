from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from rest_framework import status
from rest_framework.test import APITestCase
Model = CustomUser
class UserCreationTests(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')  # Use your actual URL name here

    def test_user_creation(self):
        user_data = {
            "username": "newuser2",
            "password": "admin",
            "email": "devxprogramming@gmail.com",
            "first_name": "New",
            "last_name": "User",
            "biography": "Does not really need to be from here"
        }
        
        response = self.client.post(self.register_url, data=user_data, format='json')
        
        # Check if the response status code is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Optionally, check if the user was created in the database
        user_exists = CustomUser.objects.filter(username=user_data['username']).exists()
        self.assertTrue(user_exists)