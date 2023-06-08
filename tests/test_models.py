from django.contrib.auth import get_user_model
from django.test import TestCase

from news.models import Newspaper, Topic


class ModelsTest(TestCase):
    def test_redactor_model_str(self):
        redactor = get_user_model().objects.create_user(
            username="user1",
            password="user_password123456",
            first_name="John",
            last_name="Smith"
        )
        self.assertEqual(str(redactor), "user1 (John Smith)")

    def test_redactor_years_experience_img_default(self):
        redactor = get_user_model().objects.create_user(
            username="user1",
            password="user_password123456",
            years_of_experience=1
        )
        self.assertEqual(redactor.username, "user1")
        self.assertEqual(redactor.years_of_experience, 1)
        self.assertEqual(redactor.img, "default.png")
        self.assertTrue(redactor.check_password("user_password123456"))

    def test_topic_str(self):
        manufacturer = Topic.objects.create(
            name="Cars"
        )
        self.assertEqual(str(manufacturer), "Cars")

    def test_newspaper_str(self):
        topic = (
            Topic.objects.create(name="Crime"),
            Topic.objects.create(name="Sport")
        )
        publishers = (
            get_user_model().objects.create_user(
                username="user1",
                password="user_password123456",
                years_of_experience=1),
            get_user_model().objects.create_user(
                username="user2",
                password="anotheruser_password123456",
                years_of_experience=4)
        )
        newspaper = Newspaper.objects.create(
            title="New newspaper",
            content="Some simple text",
        )
        newspaper.topic.set(topic)
        newspaper.publishers.set(publishers)
        self.assertEqual(str(newspaper), "New newspaper")
