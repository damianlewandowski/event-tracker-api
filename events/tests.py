from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

# Create your tests here.
from rest_framework import status
from rest_framework.fields import DateTimeField
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
import datetime
from pprint import pprint

# title = models.CharField(max_length=32)
# body = models.CharField(max_length=128)
# owner = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
# created = models.DateTimeField(auto_now_add=True)
# due_date = models.DateTimeField(blank=False)
from events.models import Event
from events.serializers import EventSerializer


EVENT_URL = reverse('event-list')


class LoginSuccessTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='damian', password='password')

    def test_login(self):
        """
        Ensure login is possible
        """
        self.assertTrue(self.client.login(username='damian', password='password'))


class EventLoginForbiddenTest(APITestCase):

    def test_auth_on_creating_event(self):
        """
        Ensure only logged in users can create events
        """
        response = self.client.post(EVENT_URL, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EventTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            "admintest",
            "admintest@admintest.com",
            "admintest"
        )
        self.client.login(username='admintest', password='admintest')
        self.data = {'title': 'Title1', 'body': 'Something about apple pie', 'due_date': datetime.date(2020, 2, 28), 'owner': self.user}
        self.event = Event.objects.create(**self.data)
        context = {'request': RequestFactory().get('/')}
        self.eventSerializer = EventSerializer(instance=self.event, context=context)

    def test_create_event(self):
        """
        Ensure we can create new events once logged in.
        """
        response = self.client.post(EVENT_URL, self.eventSerializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)  # it's 2 because one is somehow made by serializer...
        self.assertEqual(Event.objects.all()[0].title, 'Title1')


