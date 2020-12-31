import django_tables2 as tables
from django_tables2.utils import A

from .models import Cluster, Obs

class ClusterTable(tables.Table):
	root = tables.LinkColumn('clusters:analysis_page', args=[A('root')])
	class Meta:
		model = Cluster
		template_name = "django_tables2/bootstrap.html"
		fields = ("root", "z", "ra", "dec", "goodtime", "catalogue", )

class ObsTable(tables.Table):
	class Meta:
		model = Obs
		template_name = "django_tables2/bootstrap.html"
		fields = ("cluster", "obsid", "instrument", "detnam", "expgoodtime", "goodtime", "badtime", "pubdate", )
