from django.test import TestCase
from django.urls import reverse


class PortfolioSmokeTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_shows_five_featured_projects(self):
        response = self.client.get(reverse('core:home'))
        self.assertContains(response, 'Top 5')
        self.assertEqual(len(response.context['featured_projects']), 5)
