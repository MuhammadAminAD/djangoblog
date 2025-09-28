from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse


# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            email="test@gmail.com",
            password="secret"
        )

        self.post = Post.objects.create(
            title="Test title",
            body="Test body",
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title="Test title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test title')
        self.assertEqual(f'{self.post.body}', 'Test body')
        self.assertEqual(f'{self.post.author}', 'test')

    def test_post_list_view(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Test body")

    def test_post_detail_view(self):
        res = self.client.get("/post/1/")
        no_res = self.client.get("/post/1000/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(no_res.status_code, 404)
        self.assertContains(res, "Test title")
        self.assertContains(res, "Test body")
        self.assertTemplateUsed(res, "post_item.html")
