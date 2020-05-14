from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('patient1', views.PatientOneView.as_view(), name='patient1'),
    path('patient2', views.PatientTwoView.as_view(), name='patient2'),
    path('patient3', views.PatientThreeView.as_view(), name='patient3'),
    path('patient4', views.PatientFourView.as_view(), name='patient4'),
    path('starttherapy', views.TherapyView.as_view(), name='therapy'),
    path('consultdoctor', views.DoctorView.as_view(), name='doctor'),
]