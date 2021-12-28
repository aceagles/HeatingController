from django.db import models

# Create your models here.

class Temperature(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    sensor_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.sensor_name} - {self.temperature}C"

class Usage(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    is_on = models.BooleanField()

class ScheduledEvent(models.Model):
    start_time = models.DateTimeField(auto_now_add=False)
    stop_tyime = models.DateTimeField(auto_now_add=False, null=True)