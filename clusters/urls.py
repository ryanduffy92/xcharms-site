from django.urls import path

from . import views

urlpatterns = [
		path('', views.table, name='table'),
		path('<str:root>/', views.analysis_page, name='analysis page'),
]
