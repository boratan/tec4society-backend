import io

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser
from .serializers import *


# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # @csrf_exempt
    # def retrieve_all(self):
    #     queryset = Patient.objects.all()
    #     serializer = PatientSerializer(queryset, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    #
    # @csrf_exempt
    # def retrieve(self, identifier):
    #     queryset = Patient.objects.filter(id=identifier)
    #     serializer = PatientSerializer(queryset, many=True)
    #     return JsonResponse(serializer.data, safe=False)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
