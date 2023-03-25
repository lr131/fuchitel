from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    # path('login', views.login, name='login'),
    path('help', views.help_me, name='help'),
    path('search', views.SearchResultsView.as_view(), name='search'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/send/', views.send, name='send'),
     path('<int:pk>/file/', views.get_file, name='file'),
    path('<int:pk>/delete/', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)          

