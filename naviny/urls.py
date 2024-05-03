from django.urls import path
from . import views

urlpatterns = [
    path('', views.naviny_home, name='naviny_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NavinyDetailView.as_view(), name='naviny-detail'),
    path('<int:pk>/update', views.NavinyUpdateView.as_view(), name='naviny-update'),
    path('<int:pk>/delete', views.NavinyDeleteView.as_view(), name='naviny-delete'),
]