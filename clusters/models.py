from django.db import models

class Cluster(models.Model):
	root = models.CharField(verbose_name="Cluster name", max_length=50, primary_key=True)
	z = models.DecimalField(verbose_name="Redshift", max_digits=8, decimal_places=4)
	ra = models.DecimalField(verbose_name="RA", max_digits=10, decimal_places=4)
	dec = models.DecimalField(verbose_name="Dec", max_digits=10, decimal_places=4)
	goodtime = models.DecimalField(verbose_name="Clean exptime (s)",max_digits=20, decimal_places=2)
	catalogue = models.CharField(max_length=20)
