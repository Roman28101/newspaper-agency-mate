from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


from news.models import Newspaper, Topic

NEWSPAPER_LIST_URL = reverse("news:newspaper-list")
TOPIC_LIST_URL = reverse("news:topic-list")
REDACTOR_LIST_URL = reverse("news:redactor-list")


class PublicCarListTests(TestCase):
    def test_login_required(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateNewspaperListTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user1",
            password="user_password123456",
        )
        self.client.force_login(self.user)

    def test_retrieve_newspapers(self):
        topic = (Topic.objects.create(name="Crime"), Topic.objects.create(name="Sport"))
        Newspaper.objects.create(title="Some title").topic.set(topic)
        response = self.client.get(NEWSPAPER_LIST_URL)
        newspapers = Newspaper.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["newspaper_list"]), list(newspapers))

    def test_newspaper_search(self):
        topic = (Topic.objects.create(name="Crime"), Topic.objects.create(name="Sport"))
        Newspaper.objects.create(title="Some title").topic.set(topic)
        response = self.client.get(NEWSPAPER_LIST_URL)
        newspaper_search = Newspaper.objects.filter(title="Some title")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]), list(newspaper_search)
        )


class PublicTopicListTests(TestCase):
    def test_login_required(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTopicListTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user1",
            password="user_password123456",
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(name="Games")
        response = self.client.get(TOPIC_LIST_URL)
        topics = Topic.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["topic_list"]), list(topics))
        self.assertTemplateUsed(response, "news/topic_list.html")

    def test_topic_search(self):
        Topic.objects.create(name="Politics")
        response = self.client.get(TOPIC_LIST_URL)
        topic_search = Topic.objects.filter(name="Politics")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["topic_list"]), list(topic_search))


class PublicRedactorListTests(TestCase):
    def test_login_required(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorListTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user1",
            password="user_password123456",
        )
        self.client.force_login(self.user)

    def test_retrieve_redactor(self):
        get_user_model().objects.create_user(
            username="user2",
            password="another_user_password1234",
            years_of_experience=1,
        )
        get_user_model().objects.create_user(
            username="user3", password="new_user_password123456", years_of_experience=10
        )
        response = self.client.get(REDACTOR_LIST_URL)
        redactors = get_user_model().objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["redactor_list"]), list(redactors))
        self.assertTemplateUsed(response, "news/redactor_list.html")

    def test_redactor_search(self):
        response = self.client.get(REDACTOR_LIST_URL, {"username": "test3"})
        redactor_search = get_user_model().objects.filter(username="test3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["redactor_list"]), list(redactor_search))
