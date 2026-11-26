from django.test import SimpleTestCase
from django.urls import reverse

from . import content


class PortfolioSmokeTests(SimpleTestCase):
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

    def test_interview_project_page_loads(self):
        response = self.client.get(reverse('core:project_detail', kwargs={'slug': 'ai-powered-mock-interview-platform'}))
        self.assertEqual(response.status_code, 200)

    def test_insurepredict_project_page_loads(self):
        response = self.client.get(reverse('core:project_detail', kwargs={'slug': 'insurepredict-insurance-cost-prediction'}))
        self.assertEqual(response.status_code, 200)

    def test_apple_dashboard_project_page_loads(self):
        response = self.client.get(reverse('core:project_detail', kwargs={'slug': 'apple-product-pricing-dashboard'}))
        self.assertEqual(response.status_code, 200)

    def test_featured_projects_have_required_detail_data(self):
        required = ('description', 'problem_statement', 'solution', 'architecture', 'features_list', 'dataset_info', 'results', 'challenges', 'future_improvements')
        for project in content.PROJECTS:
            if project.is_featured:
                for field in required:
                    self.assertTrue(getattr(project, field), f'{project.slug} is missing {field}')

    def test_projects_api_returns_five_featured_projects(self):
        response = self.client.get(reverse('core:api_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_github_api_returns_success_payload(self):
        response = self.client.get(reverse('core:api_github'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

    def test_api_overview_is_available(self):
        response = self.client.get(reverse('core:api_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('projects', response.json())

    def test_featured_project_github_links_are_present(self):
        for project in content.PROJECTS:
            if project.is_featured:
                self.assertTrue(project.github_url.startswith('https://github.com/'))

    def test_projects_are_sorted_by_order(self):
        featured = [project for project in content.PROJECTS if project.is_featured]
        self.assertEqual([project.order for project in featured], sorted(project.order for project in featured))

    def test_current_experience_is_marked_current(self):
        current = [item for item in content.EXPERIENCE if item.is_current]
        self.assertEqual(len(current), 1)
        self.assertEqual(current[0].company, 'Plainsurf Solutions Pvt Ltd')

    def test_project_detail_contains_required_sections(self):
        response = self.client.get(reverse('core:project_detail', kwargs={'slug': 'apple-product-pricing-dashboard'}))
        self.assertContains(response, 'Architecture')
        self.assertContains(response, 'Results')
        self.assertContains(response, 'Future Improvements')
