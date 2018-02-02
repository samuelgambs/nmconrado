from django.shortcuts import render
from nmcapp.models import Services, Trainings

# Create your views here.
def home(request):

	results = Services.objects.all()
	results_active = results.filter(status=1)

	return render(request, 'index.html', context={
		"services": results_active,
		"request": request
	})

def services(request):
	return render(request, 'services.html')
			
def about(request):
	return render(request, 'about.html')	


