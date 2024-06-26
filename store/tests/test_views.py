from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from store.models import Category, Products
from store.views import *


class TestViewresponse(TestCase):


    def setUp(self):
        self.c = Client()
        User.objects.create(username = 'admin')
        Category.objects.create(name = 'django', slug = 'django')
        Products.objects.create(category_id = 1, title = 'django beginners',
                                created_by_id= 1, slug = 'django-beginners',
                                price = 20.00, image = 'django')

    # test for homepage
    def test_homepage_url(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    # test product_detail url

    def test_productdetail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    
    # test category response status
    def test_category_detail_url(self):
        res =self.c.get(reverse('store:categories', args=['django']))
        self.assertEqual(res.status_code, 200)

    def test_homepage_template(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title> Home </title>',html)


    



    