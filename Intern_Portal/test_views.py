import pytest
from django.urls import reverse
from django.test import Client
from .models import Circular

@pytest.mark.django_db
def test_circular_view(client):
    # Create a Circular object
    Circular.objects.create(subject='Test Subject', message='Test Message')

    # Access the circular view
    response = client.get(reverse('circular'))

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the Circular object is present in the context
    assert 'circ' in response.context
    assert len(response.context['circ']) == 1

@pytest.mark.django_db
def test_main_dashboard_view(client):
    # Access the main dashboard view
    response = client.get(reverse('main_dashboard'))

    # Check if the response status code is 200
    assert response.status_code == 200

@pytest.mark.django_db
def test_student_login_view(client):
    # Access the student login view with a POST request
    response = client.post(reverse('Student_Login'))

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the error message is present in the context
    assert 'error_message' in response.context

@pytest.mark.django_db
def test_student_dashboard_view(client):
    # Access the student dashboard view
    response = client.get(reverse('student_dashboard'))

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if circulars are present in the context
    assert 'circulars' in response.context
