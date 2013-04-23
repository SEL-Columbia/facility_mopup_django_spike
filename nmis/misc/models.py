from django.db import models

class LGA(models.Model):
	name = models.TextField()
	unique_slug = models.TextField()
