from django.contrib import admin
from nmcapp.models import Services, Training

class ServicesAdmin(admin.ModelAdmin):
	list_display = ['title', 'subtitle']

class TrainingAdmin(admin.ModelAdmin):
	list_display = ['title', 'subtitle']	
	
admin.site.register(Services,ServicesAdmin)
admin.site.register(Training,TrainingAdmin)    