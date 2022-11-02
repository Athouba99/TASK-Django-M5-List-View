"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights.views import BookingListView, FlightListView, BookingDetailListView, BookingUpdateListView,DeleteBookingListView
from users.views import RegisterAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Task 1: list view 
    path("flights/", FlightListView.as_view(), name="flights-list"),
    path("booking/", BookingListView.as_view(), name="booking-list"), 
    # Task 2: API CRUD 
    path("details/<int:object_id>/",BookingDetailListView.as_view(), name="booking-details"),
    path("update/", BookingUpdateListView.as_view(), name="booking-update"),
    path("delete/", DeleteBookingListView.as_view(), name="cancel-booking"),
    # Task 3: Register view  
    path("register/", RegisterAPIView.as_view(), name="register"),
     

]
