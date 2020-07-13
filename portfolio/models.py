from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Portfolio')
    url = models.URLField(blank=False, default='http://localhost:8000')
    image = models.URLField(blank=False, default='http://localhost:8000')

    def __str__(self):
        return self.name