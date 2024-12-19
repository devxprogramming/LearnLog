from django.test import TestCase
from .models import LearnLog
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

Model = get_user_model()

class LearnLogTest(APITestCase):

    def test_learnlog_create(self):
        data = {
            'title': 'This is a test title',
            'content': 'This is a test content',
            'priority': 'High',
            'progress': 'New',
        }
        response = self.client.post(reverse('create_log'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)