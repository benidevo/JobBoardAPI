from rest_framework.test import APIClient,  APITestCase
from api.models import JobOffer
from datetime import datetime

# Create your tests here.

class TestJobofferModel(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.job_offer = JobOffer

    def test_create_job_offer(self):
        """ test that a job offer was successfully created """

        company_name = 'Access Bank'
        company_email = 'contact@accessbank.com'
        job_title = 'Bank Teller'
        job_description = 'Ensure that customers make their deposits and withdrawals on time in the banking hall'
        salary = 30000
        city = 'Ikeja'
        state = 'Lagos'
        created_at = datetime.now()
        is_available = True

        offer = self.job_offer(company_name=company_name, company_email=company_email, job_title=job_title, job_description=job_description, salary=salary, city=city, state=state, created_at=created_at, is_available=is_available)
        
        self.assertEqual(offer.company_name, 'Access Bank')
        self.assertEqual(type(offer.salary), int)
