from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register/',register,name='register'),
    path('about/',about, name='about'),
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('services/',services, name='services'),
    path('events/',events, name='events'),
    path('blog/',blog, name='blog'),
    path('team/<int:id>/',team, name='team'),
    path('all_team_member/',all_team_member, name='all_team_member'),
    path('testimonials/',testimonials, name='testimonials'),
    path('contact/',contact, name='contact'),
    path('service_provider_reg/',service_provider_reg, name='service_provider_reg'),
    path('service_prov_log/',service_prov_log, name='service_prov_log'),
    path('book_pro/<int:id>/',book_pro, name='book_pro'),
    path('your_bookings/', your_bookings, name='your_bookings'),
    path('cancel_booking/<int:id>/',cancel_booking,name='cancel_booking'),
    path('bookings_request/', bookings_request, name='bookings_request'),
    path('accept_booking/<int:id>/', accept_booking, name='accept_booking'),
]