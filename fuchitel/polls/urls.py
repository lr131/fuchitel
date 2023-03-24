from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help_me, name='help'),
    path('search', views.SearchResultsView.as_view(), name='search'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/send/', views.send, name='send'),
    path('<int:pk>/delete/', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)          

