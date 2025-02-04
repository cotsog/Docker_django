import datetime
from django.test import TestCase
from .models import Question
from django.utils import timezone
from django.urls import reverse
# Create your tests here.
#import pytest

# def n_days_ago(n):
#     return timezone.now() - datetime.timedelta(days=n)
#
#
# def n_days_later(n):
#     return timezone.now() + datetime.timedelta(days=n)
#
#
# def test_was_published_recently_with_future_question():
#     next_month = timezone.now() + datetime.timedelta(days=30)
#     future_question = Question('Back from the future', pub_date=next_month)
#     assert not future_question.was_published_recently()
#
#
# def test_was_published_recently_with_old_question():
#     last_year = timezone.now() - datetime.timedelta(days=365)
#     old_question = Question('Why is there something instead of nothing?', pub_date=last_year)
#     assert not old_question.was_published_recently()
#
#
#
#
#
# def create_question(question_text, pub_date=None):
#     if not pub_date:
#         pub_date = timezone.now()
#     return Question.objects.create(question_text=question_text, pub_date=pub_date)
#
#
# def get_latest_list(client):
#     response = client.get(reverse('polls:index'))
#     assert response.status_code == 200
#     return response.context['latest_question_list']
#
#
# def assert_question_list_equals(actual_questions, expected_texts):
#     assert len(actual_questions) == len(expected_texts)
#     for actual_question, expected_text in zip(actual_questions, expected_texts):
#         assert actual_question.question_text == expected_text
#
#
# def assert_no_polls(text):
#     assert "No polls are available." in text
#
#
#
#
# @pytest.mark.django_db
# def test_past_question(client):
#     create_question(question_text="Past question.", pub_date=n_days_ago(30))
#     latest_list = get_latest_list(client)
#     assert_question_list_equals(latest_list, ["Past question."])
#
#
# @pytest.mark.django_db
# def test_future_question(client):
#     create_question(question_text="Future question.", pub_date=n_days_later(30))
#     response = client.get(reverse('polls:index'))
#     assert_no_polls(response.rendered_content)
#     latest_list = get_latest_list(client)
#     assert not latest_list
#
#
# @pytest.mark.django_db
# def test_future_question_and_past_question(client):
#     create_question(question_text="Past question.", pub_date=n_days_ago(30))
#     create_question(question_text="Future question.", pub_date=n_days_later(30))
#     latest_list = get_latest_list(client)
#     assert_question_list_equals(latest_list, ["Past question."])
#
#
# @pytest.mark.django_db
# def test_two_past_questions(client):
#     create_question(question_text="Past question 1.", pub_date=n_days_ago(30))
#     create_question(question_text="Past question 2.", pub_date=n_days_ago(5))
#     latest_list = get_latest_list(client)
#     expected_texts = ["Past question 2.", "Past question 1."]
#     assert_question_list_equals(latest_list, expected_texts)
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTest(TestCase):

    def test_question_with_no_response(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEquals(response.status_code, 200);
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])