from django.db import models

class Cluster(models.Model):
	root = models.CharField(max_length=50, primary_key=True)
	z = models.DecimalField(max_digits=8, decimal_places=4)
	ra = models.DecimalField(max_digits=10, decimal_places=4)
	dec = models.DecimalField(max_digits=10, decimal_places=4)
	goodtime = models.DecimalField(max_digits=20, decimal_places=2)
	catalogue = models.CharField(max_length=20)
