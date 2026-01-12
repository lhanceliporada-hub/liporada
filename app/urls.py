from django.urls import path, include
from .views import (HomePageView, AboutPageView,EcoConnectListView,EcoConnectDetailView,
                    EcoConnectCreateView,
                    EcoConnectUpdateView, EcoConnectDeleteView, toggle_like,
                    ArticleListView, ProjectListView, EventListView, GreenBusinessListView,
                    ArticleCreateView,  ProjectCreateView, EventCreateView, GreenBusinessCreateView,
                    ArticleDetailView, ProjectDetailView, EventDetailView, GreenBusinessDetailView,
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ecoConnect/<int:pk>/like/', toggle_like, name='toggle_like'),
    path('ecoConnect/', EcoConnectListView.as_view(), name='ecoConnect_list'),
    path('ecoConnect/<int:pk>/', EcoConnectDetailView.as_view(), name='ecoConnect_detail'),
    path('ecoConnect/create/', EcoConnectCreateView.as_view(), name='ecoConnect_create'),
    path('ecoConnect/<int:pk>/edit/', EcoConnectUpdateView.as_view(), name='ecoConnect_update'),
    path('ecoConnect/<int:pk>/delete/', EcoConnectDeleteView.as_view(), name='ecoConnect_delete'),

    path('articles/', ArticleListView.as_view(), name='articles'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('events/', EventListView.as_view(), name='events'),
    path('businesses/', GreenBusinessListView.as_view(), name='businesses'),

    # ARTICLES
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),

    # PROJECTS
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

    # EVENTS
    path('events/', EventListView.as_view(), name='events'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),

    # BUSINESSES
    path('businesses/', GreenBusinessListView.as_view(), name='businesses'),
    path('businesses/create/', GreenBusinessCreateView.as_view(), name='business_create'),
    path('businesses/<int:pk>/', GreenBusinessDetailView.as_view(), name='business_detail'),


]