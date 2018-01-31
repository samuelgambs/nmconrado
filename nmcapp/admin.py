from django.contrib import admin
from nmcapp.models import Services, Trainings

class ServicesAdmin(admin.ModelAdmin):
	list_display = ['title', 'subtitle']

class TrainingsAdmin(admin.ModelAdmin):
	list_display = ['title', 'subtitle']	
	
admin.site.register(Services,ServicesAdmin)
admin.site.register(Trainings,TrainingsAdmin)    