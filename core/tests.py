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

    def test_target_profile_is_consistent(self):
        response = self.client.get(reverse('core:home'))
        target = 'Aspiring AI/ML Engineer | Data Scientist | Generative AI & RAG Developer | Data Analyst | Python Developer'
        self.assertContains(response, target)
        self.assertEqual(content.PROFILE.title, target)

    def test_programming_skills_exclude_removed_languages(self):
        programming = [skill.name.lower() for skill in content.SKILLS if skill.category == 'PROGRAMMING']
        self.assertNotIn('java', programming)
        self.assertNotIn('r', programming)

    def test_general_resume_uses_uploaded_pdf(self):
        response = self.client.get(reverse('core:home'))
        self.assertContains(response, '/static/media/resumes/roles/Resume.pdf')
        self.assertTrue(content.PROFILE.resume_pdf.url.endswith('Resume(AI_ML).pdf'))

    def test_document_project_page_loads(self):
        response = self.client.get(reverse('core:project_detail', kwargs={'slug': 'ai-powered-document-intelligence-rag-assistant'}))
        self.assertEqual(response.status_code, 200)

    def test_loan_project_page_loads(self):
        response = self.client.get(reverse('core:project_detail', kwargs={'slug': 'intelligent-loan-risk-assessment-prediction-platform'}))
        self.assertEqual(response.status_code, 200)
