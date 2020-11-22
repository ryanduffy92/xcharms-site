from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Cluster

def table(request):
	all_clusters = Cluster.objects.order_by('z')
	context = {'all_clusters': all_clusters}
	return render(request, 'clusters/table.html', context)

def analysis_page(request, root):
	cluster = get_object_or_404(Cluster, pk=root)
	return render(request, 'clusters/analysis_page.html', {'cluster': cluster})
