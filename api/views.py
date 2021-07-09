from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from api.models import JobOffer
from api.serializers import JobOfferSerializer
from utils.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

class JobOffers(APIView):
    parser_classes = (MultiPartParser, JSONParser, FormParser)

    def get(self, request):
        offers = JobOffer.objects.all()
        serializer = JobOfferSerializer(offers, many=True)
        return Response(data={'job offers': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'status': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobOffersById(APIView):

    def get(self, request, id):

        offer = JobOffer.objects.get(id=id)
        serializer = JobOfferSerializer(offer)
        return Response(data={'job offer': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id):
        update_job = get_object_or_404(JobOffer, id=id)
        serializer = JobOfferSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.instance = update_job
            serializer.save()
            return Response(data={'message': 'you have successfully updated your job ad'}, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        