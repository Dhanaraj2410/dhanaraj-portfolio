from django.core import mail
from django.test import TestCase, override_settings

from .models import ContactMessage


class ContactSubmissionTests(TestCase):
    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        EMAIL_HOST='smtp.example.com',
        CONTACT_EMAIL='owner@example.com',
        DEFAULT_FROM_EMAIL='sender@example.com',
    )
    def test_contact_submission_sends_configured_notification(self):
        response = self.client.post(
            '/contact/submit/',
            {
                'name': 'Recruiter',
                'email': 'recruiter@example.com',
                'company': 'Example Inc',
                'job_role': 'Engineer',
                'message': 'I would like to discuss an opportunity.',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['owner@example.com'])
        self.assertEqual(mail.outbox[0].from_email, 'sender@example.com')
