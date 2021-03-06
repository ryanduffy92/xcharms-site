from django.db import models

class Cluster(models.Model):
	root = models.CharField(verbose_name="Cluster name", max_length=50, primary_key=True)
	z = models.DecimalField(verbose_name="Redshift", max_digits=8, decimal_places=4)
	ra = models.DecimalField(verbose_name="RA", max_digits=10, decimal_places=4)
	dec = models.DecimalField(verbose_name="Dec", max_digits=10, decimal_places=4)
	goodtime = models.DecimalField(verbose_name="Clean exptime (s)", max_digits=20, decimal_places=2)
	catalogue = models.CharField(max_length=20)

class Obs(models.Model):
	cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
	obsid = models.IntegerField(verbose_name="ObsID")
	instrument = models.CharField(verbose_name="Detector", max_length=6)
	detnam = models.CharField(verbose_name="Detector CCDs", max_length=15)
	expgoodtime = models.DecimalField(verbose_name="Expected length (ks)", max_digits=20, decimal_places=2)
	goodtime = models.DecimalField(verbose_name="Good time (s)", max_digits=20, decimal_places=2)
	badtime = models.DecimalField(verbose_name="Bad time (s)", max_digits=20, decimal_places=2)
	pubdate = models.DateField(verbose_name="Public Date")
