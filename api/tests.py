from numbers import Number
from re import A
import re
from rest_framework.test import APIClient,  APITestCase
from api.models import JobOffer
from datetime import datetime
from rest_framework import status

# Create your tests here.
client = APIClient()
BASE_URL = 'https://localhost:8000/api/'
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


class TestPostAndGetJobsEndpoint(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_job(self):
        response = self.client.get(BASE_URL + 'jobs')
        self.assertEqual(response.status_code, 200)

    def test_post_job(self):
        
        payload = {
            "company_name": "Access Bank",
            "company_email": "info@accessdlbank.com",
            "job_title": "Bank Teller",
            "job_description": "Ensure that customers are attended to promptly",
            "salary": 90000,
            "city": "Ikeja",
            "state": "Lagos",
            "is_available": True
        }
        response = self.client.post(BASE_URL + 'jobs', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestGetPUTAndDeleteJobEndpoint(APITestCase):

    def test_get_job_by_id(self):
        payload = {
            "company_name": "Access Bank",
            "company_email": "info@accessdlbank.com",
            "job_title": "Bank Teller",
            "job_description": "Ensure that customers are attended to promptly",
            "salary": 90000,
            "city": "Ikeja",
            "state": "Lagos",
            "is_available": True
        }
        res = client.post(BASE_URL +'jobs', payload)
        id = res.data['data']['status']['id']
        response = client.get(BASE_URL +'jobs/' + id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_job_by_id(self):
        payload = {
            "company_name": "Access Bank",
            "company_email": "info@accessdlbank.com",
            "job_title": "Bank Teller",
            "job_description": "Ensure that customers are attended to promptly",
            "salary": 90000,
            "city": "Ikeja",
            "state": "Lagos",
            "is_available": True
        }
        res = client.post(BASE_URL +'jobs', payload)
        id = res.data['data']['status']['id']

        response = client.put(BASE_URL +'jobs/' + id, {"company_name": "Zenith Bank",})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

