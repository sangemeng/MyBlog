from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mysite_index'),
    path('last_index/<int:indexes>/', views.last_index, name='mysite_last_index'),
    path('next_index/<int:indexes>/', views.next_index, name='mysite_next_index'),
    path('indexes=<int:indexes>/', views.index_indexes, name='mysite_indexes'),
    path('page/<slug:slug>/', views.page, name='mysite_page'),
    path('message/', views.message, name='mysite_message'),
    path('add_message/', views.add_message, name='mysite_add_message'),
]
