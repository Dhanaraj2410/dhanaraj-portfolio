from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APITestCase


class AIRequestValidationTests(APITestCase):
    @patch('ai_assistant.views.chat_with_ai')
    def test_chat_rejects_non_string_messages(self, chat_with_ai):
        for message in (123, [], {}):
            with self.subTest(message=message):
                response = self.client.post(
                    '/api/ai/chat/',
                    {'message': message},
                    format='json',
                )

                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        chat_with_ai.assert_not_called()

    @patch('ai_assistant.views.analyze_resume_match')
    def test_resume_analysis_rejects_non_string_job_descriptions(self, analyze):
        for description in (123, [], {}):
            with self.subTest(description=description):
                response = self.client.post(
                    '/api/ai/resume-analysis/',
                    {'job_description': description},
                    format='json',
                )

                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        analyze.assert_not_called()

    @patch('ai_assistant.views.chat_with_ai', return_value={'success': True})
    def test_chat_trims_message_before_processing(self, chat_with_ai):
        response = self.client.post(
            '/api/ai/chat/',
            {'message': '  Hello  '},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        chat_with_ai.assert_called_once_with('Hello')
