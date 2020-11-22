from django.urls import path

from . import views

app_name = 'clusters'
urlpatterns = [
		path('', views.table, name='table'),
		path('<str:root>/', views.analysis_page, name='analysis_page'),
]
