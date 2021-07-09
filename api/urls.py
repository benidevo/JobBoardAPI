from django.urls import path
from api.views import JobOffers, JobOffersById

urlpatterns = [
    path('jobs', JobOffers.as_view(), name='jobs'),
    path('jobs/<id>', JobOffersById.as_view(), name='job')
]