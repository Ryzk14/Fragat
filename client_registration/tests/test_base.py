from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains
from django.test import TestCase

class TestHomePage(TestCase):

    def test_homepage_200(self):
        response = self.client.get('')
        assert response.status_code == 200

    def test_homepage_by_name(self):
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_template_home_is_correct(self):  # new
        response = self.client.get(reverse('home'))
        assertTemplateUsed(response, 'client_registration/home.html')

    def test_template_home_h1(self):  # new
        response = self.client.get(reverse('home'))
        assertContains(response, '<h1>Homepage</h1>')

class TestAboutPage(TestCase):

    def test_about_200(self):
        response = self.client.get('/about/')
        assert response.status_code == 200


    def test_about_by_name(self):
        response = self.client.get(reverse('about'))
        assert response.status_code == 200

    def test_template_about_is_correct(self):  # new
        response = self.client.get(reverse('about'))
        assertTemplateUsed(response, 'client_registration/about.html')

    def test_template_about_h1(self): # new
        response = self.client.get(reverse('about'))
        assertContains(response, '<h1>About page</h1>')



