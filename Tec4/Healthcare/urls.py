from django.urls import path, include
from rest_framework import routers

from Healthcare import views

router = routers.DefaultRouter()
router.register(r'patient/', views.PatientViewSet, basename='Patient')
router.register(r'request/', views.PatientViewSet, basename='Request')

urlpatterns = [
    path('', include(router.urls)),

    # patient stuff
    path('Patient/', views.PatientViewSet.retrieve_all),
    path('Patient/<int:identifier>', views.PatientViewSet.retrieve),

    # request stuff
    path('Request/', views.RequestViewSet.retrieve_all),
    path('Request/<int:identifier>', views.RequestViewSet.retrieve),

    # get everything else

]
