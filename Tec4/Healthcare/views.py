import io

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser
from .serializers import *


# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):

    @csrf_exempt
    def retrieve_all(self):
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def retrieve(self, identifier):
        queryset = Patient.objects.filter(id=identifier)
        serializer = PatientSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class RequestViewSet(viewsets.ModelViewSet):

    @csrf_exempt
    def retrieve_all(self):
        queryset = Request.objects.all()
        serializer = RequestSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def retrieve(self, identifier):
        queryset = Request.objects.filter(id=identifier)
        serializer = RequestSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


# borislav upload kubernetes + ask about children