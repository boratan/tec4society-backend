from django.urls import path, include
from rest_framework import routers

from Healthcare import views

router = routers.DefaultRouter()
router.register(r'patient', views.PatientViewSet)
router.register(r'request', views.RequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('requestChain/', views.post),
    path('approveChain/', views.vote),

    # patient stuff
    # path('Patient/', views.PatientViewSet.retrieve_all),
    # path('Patient/<int:identifier>', views.PatientViewSet.retrieve),


]
