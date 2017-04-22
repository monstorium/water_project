#watersourcereport/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required

from .models import WaterSourceReport
from .forms import WaterSourceReportForm

# Create your views here.

# @login_required
# def create(request):
# 	return render(request, 'watersourcereport/create.html')

class WaterSourceReportPage(FormView):
	template_name = 'create.html'
	success_url ='/created the report yay/'
	form_class = WaterSourceReportForm

	def form_valid(self, form):
		return HttpResponse("The form is valid.")