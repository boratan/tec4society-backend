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

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return RequestSerializerWrite
        else:
            return RequestSerializer


class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


# custom post method meant for accessing the  chaincode API
@csrf_exempt
def post(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)

        serializer = RequestSerializer(data=data)
        if serializer.is_valid():

            #

            serializer.save()
            response = JsonResponse(serializer.data, safe=False)
            response["Access-Control-Allow-Origin"] = "*"
        else:
            print(serializer.errors)
            existing_request = RequestSerializer(Request.objects.get(id=data["id"]))
            response = JsonResponse(existing_request.data, safe=False)
        return response


# getting specific objects
@csrf_exempt
def get(request):

    if request.method == 'GET':
        # query = Request.objects.raw('SELECT * FROM healthcare_request')
        query = Request.objects.raw.get("SELECT * FROM healthcare_request r")# how to get only select???

        serializer = RequestSerializer(query, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def put(request):

    if request.method == 'PUT':
        # query = Request.objects.raw('SELECT * FROM healthcare_request')
        query = Request.objects.raw('SELECT id FROM healthcare_request r')# how to get only select???

        serializer = RequestSerializer(query, many=True)
        return JsonResponse(serializer.data, safe=False)

