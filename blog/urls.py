from django.urls import path

from django.urls import path

from .views import HomeView, AboutView, NewsListView, NewsDetailView, ContactView

urlpatterns = [    path('', HomeView.as_view(), name='home'),   
                path('about/', AboutView.as_view(), name='about'),    
                path('news/', NewsListView.as_view(), name='news_list'),    
                path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),    
                path('contact/', ContactView.as_view(), name='contact'),]
