from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
								  DetailView,CreateView,
								  UpdateView,DeleteView)
# Create your views here.

class IndexView(TemplateView):
	template_name = 'index.html'

class PatientOneView(TemplateView):
	template_name = 'patient1.html'

class PatientTwoView(TemplateView):
	template_name = 'patient2.html'

class PatientThreeView(TemplateView):
	template_name = 'patient3.html'

class PatientFourView(TemplateView):
	template_name = 'patient4.html'


class TherapyView(TemplateView):
	template_name = 'therapy.html'

class DoctorView(TemplateView):
	template_name = 'doctor.html'
