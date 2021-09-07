from django.contrib import admin
from models.models import Temperature, Usage, ScheduledEvent
# Register your models here.
admin.site.register(Temperature)
admin.site.register(Usage)
admin.site.register(ScheduledEvent)