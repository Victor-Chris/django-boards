from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Board, Topic, Post
from ..views import PostUpdateView

class PostUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all post_update_view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django Board')
        self.username = 'john'
        self.password = 'abcdef1235'
        user = User.objects.create_user(username=self.username, email='john@gmail.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello there', board=self.board, starter=user)
        self.post = Post.objects.create(message='This is a test post', topic=self.topic, created_by=user)
        self.url = reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })

class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def test_redirection(self):
        '''
        Test to check if only logged in users can edit posts
        '''
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        '''
        Create a different user from the one who created the post
        '''
        super().setUp()
        username='jane'
        password='randpass'
        user = User.objects.create_user(username=username, email='jane@gmail.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        '''
        Topic should only be editable by the owner. Unauthorizes users should get a 404 error.
        '''
        self.assertEqual(self.response.status_code, 404)

class PostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        pass

class SuccessfulPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        pass

class InvalidPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        pass
