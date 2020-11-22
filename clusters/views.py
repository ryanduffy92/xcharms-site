from django.shortcuts import render
from django.http import HttpResponse

from .models import Cluster

def table(request):
	all_clusters = Cluster.objects.order_by('z')
	context = {'all_clusters': all_clusters}
	return render(request, 'clusters/table.html', context)
	#return HttpResponse("This is where the table of clusters goes.")

def analysis_page(request, root):
	return HttpResponse("This will display the cluster analysis of the cluster with root {}.".format(root))
