import pytest
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from model_bakery import baker

from main.models import Message


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def user():
    return User.objects.create_user('test1')


@pytest.fixture()
def message_factory():
    def factory(*args, **kwargs):
        return baker.make(Message, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_messages(client, user, message_factory):
    messages = message_factory(_quantity=10)

    response = client.get('/messages/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(messages)
    for i, m in enumerate(data):
        assert m['text'] == messages[i].text


@pytest.mark.django_db
def test_create_message(client, user):
    count = Message.objects.count()

    response = client.post('/messages/', data={'user': user.id, 'text': 'tt'})


    assert response.status_code == 201
    assert Message.objects.count() == count + 1

