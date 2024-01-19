from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.dashboard, name='dashboard'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('lists', views.book_desc, name='book_desc'),
    path('maths', views.list1, name='maths'),
    path('chemistry', views.list2, name='chemistry'),
    path('english', views.list3, name='english'),
    path('tutorials', views.book_list, name='book_list'),
    path('tutorials/<int:pk>/', views.book_detail, name='book_detail'),
    path('tutorials/new/', views.book_create, name='book_create'),
    path('tutorials/<int:pk>/edit/', views.book_update, name='book_update'),
    path('tutorials/<int:pk>/delete/', views.book_delete, name='book_delete'),
]