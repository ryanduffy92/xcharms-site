from django.contrib import admin

from .models import Cluster, Obs

admin.site.register(Cluster)
admin.site.register(Obs)
