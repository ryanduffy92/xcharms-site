from django.urls import path

from . import views

app_name = 'clusters'
urlpatterns = [
		path('', views.ClusterListView.as_view()),
		path('<str:root>/', views.analysis_page, name='analysis_page'),
]
