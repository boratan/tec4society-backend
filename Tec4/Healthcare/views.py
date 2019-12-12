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


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


# custom post method meant for accessing the  chaincode API
@csrf_exempt
def post(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = RequestSerializer(data=data)
        if serializer.is_valid():

            # Send the request to CHAINCODE here

            serializer.save()
            response = JsonResponse(serializer.data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
        else:
            print(serializer.errors)
            existing_request = RequestSerializer(Request.objects.get(id=data["id"]))
            response = JsonResponse(existing_request.data, safe=False)
        return response


@csrf_exempt
def vote(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = RequestSerializer(data=data)
        if serializer.is_valid():

            # Send the request to CHAINCODE here

            serializer.save()
            response = JsonResponse(serializer.data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
        else:
            print(serializer.errors)
            existing_request = RequestSerializer(Request.objects.get(id=data["id"]))
            response = JsonResponse(existing_request.data, safe=False)
        return response
