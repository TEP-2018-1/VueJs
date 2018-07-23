from django.test import *
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import *
from rest_framework import status
import json
import requests

# python manage.py dumpdata -o text_fixtures.json --exclude=contenttypes
# python manage.py test aplicacao.tests
class APITest(TestCase):

  fixtures = ['fixtures.json']

  def test_pessoa_list(self):
    response = self.client.get(reverse('pessoa-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_pessoa_detail(self):
    response = self.client.get(reverse('pessoa-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_list(self):
    response = self.client.get(reverse('post-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_detail(self):
    response = self.client.get(reverse('post-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_comment_list(self):
    response = self.client.get(reverse('comment-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_comment_detail(self):
    response = self.client.get(reverse('comment-detail', args=[1]))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_new_pessoa(self):
    request_data = {"id": 1,
                    "email": "Jose@hotmail.com",
                    "name": "Antonette"}
    response = self.client.put(reverse('pessoa-list'), data=request_data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_new_post_not_auth(self):
    response = json.dumps({"title": "new post",
                        "body": "body of post",
                        "user": "Bret"})
    resultado = requests.post('http://127.0.0.1:8000/posts/', data=response, headers={'content-type': 'application/json'})
    self.assertEqual(resultado.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_new_post_auth(self):
    response = json.dumps({"title": "new post",
                    "body": "body of post",
                    "user": "Bret"})
    resultado = requests.post('http://127.0.0.1:8000/posts/', data=response, headers={'content-type': 'application/json'}, auth=('Bret', '123'))
    self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)

  def test_new_comment(self):
    response = json.dumps({'name': 'Bret',
                        'email': 'bret@hotmail.com',
                        'body': 'post test',
                        'post': 'http://127.0.0.1:8000/posts/50/'})
    resultado = requests.post('http://127.0.0.1:8000/comments/', data=response, headers={'content-type': 'application/json'}, auth=('Bret', '123'))
    self.assertEqual(resultado.status_code, status.HTTP_201_CREATED)

  def test_delete_comment_outher_user(self):
    resultado = requests.delete('http://127.0.0.1:8000/comments/100/', auth=('Bret','123'))
    self.assertEqual(resultado.status_code, status.HTTP_403_FORBIDDEN)


  def test_delete_comment_not_user(self):
    resultado = requests.delete('http://127.0.0.1:8000/comments/19/', auth=('Bret', '123'))

    self.assertEqual(resultado.status_code, status.HTTP_204_NO_CONTENT)

