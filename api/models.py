from django.db import models
import uuid

class JobOffer(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField(max_length=255, unique=True)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    salary = models.IntegerField()
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.company_name}: {self.job_title}'