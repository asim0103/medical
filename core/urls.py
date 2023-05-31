from django.urls import path
from core import views
from core.views import *

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.home2, name='home'),

    
    path('faq', views.faq, name='faq'),    
    path('about', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('search/', views.search, name='search'),
    path('doctors', DoctorsListView.as_view(),  name='doctors'),
    path('doctors/<slug:slug>/', DoctorsDetailView.as_view(), name='detail_doctors'),
    
    path('services', views.services,  name='services'),
    path('services/<slug:slug>', views.service_details , name='service_detail'),
    
    # path('contact_us', views.contact_us, name='contact_us'),
    
    # path('doctor_details_2', views.doctor_details_2, name='doctor-details-2'),
    
    # path('doctor_details', views.doctor_details, name='doctor-details'),
    
    # path('blog_single_standart', views.blog_single_standart, name='blog_single_standart'),
    
    # path('blog_single', views.blog_single, name='blog_single'),
    
    
    path('blog_classic/<int:id>', views.blog_single, name='blog_single'),
    
    
    path('blog_classic', views.blog_classic, name='blog-classic'),
    
    path('blog_grid', views.blog_grid, name='blog-grid'),
    
    path('blog_list', views.blog_list, name='blog-list'),
    
    path('blog_single_2', views.blog_single_2, name='blog-single'),
    
    path('contact', views.contact, name='contact_us'),
    
    
    
]
