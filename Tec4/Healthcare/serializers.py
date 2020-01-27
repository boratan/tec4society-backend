from rest_framework import serializers

from rest_framework.fields import SerializerMethodField
from .models import *



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):

    # patientId = PatientSerializer(read_only=True)
    # patientId_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), write_only=True)

    class Meta:
        depth = 1
        model = Request
        fields = "__all__"


class RequestSerializerWrite(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = "__all__"


# def get_serializer_class(self):
#     method = self.request.method
#     if method == 'PUT' or method == 'POST':
#         return YourWriteSerializer
#     else:
#         return RequestSerializer



