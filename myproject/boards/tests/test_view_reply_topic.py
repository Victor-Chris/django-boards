from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Board, Topic, Post
from ..views import reply_topic

class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all reply_topic view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django Board")
        self.username = "John"
        self.password = "abcde12345"
        user = User.objects.create_user(username=self.username, email="john@gmail.com", password=self.password)
        self.topic = Topic.objects.create(subject="Hello there", board=self.board, starter=user)
        Post.objects.create(message="Sample message", topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={ 'pk': self.board.pk, 'topic_pk': self.topic.pk })

class LoginRequiredReplyTests(ReplyTopicTestCase):
    def rand_test(self):
        pass
    # ...

class ReplyTopicTests(ReplyTopicTestCase):
    def rand_test(self):
        pass
    # ...

class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    def rand_test(self):
        pass
    # ...

class InvalidReplyTopicTests(ReplyTopicTestCase):
    def rand_test(self):
        pass
    # ...
    