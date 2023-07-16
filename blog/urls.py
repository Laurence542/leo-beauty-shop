from django.conf.urls.static import static
from django.conf import settings
from . import views
from.views import about
from.views import feature
from .views import admin_homepage
from .views import hotel_view
from .views import addservices
from .views import booking_appointment
from .views import payment_methods
from .views import credit_card
from .views import sucess_message
from .views import booking_view
from .views import ourservices
from .views import contact_us
from .views import booking_views
from .views import create_employees
from .views import client_views
from .views import view_employe
from .views import clientslogin
from .views import delete_post
from .views import clients_signup
from .views import employelogins
from .views import create_admin_signups
from .views import create_admin_logins
from .views import employeesignup
from.views import assign_case
from .views import action_bookings
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('assign/<int:booking_id>/', assign_case, name='assign_case'),
    path('about/',about, name = "about"),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('action_booking/',action_bookings, name = "action_booking"),
    path('create_employe/',create_employees, name = "create_employe"),
    path('create_admin_signup/',create_admin_signups, name = "create_admin_signup"),
    path('create_admin_login/',create_admin_logins, name = "create_admin_login"),
    path('view_employee/',view_employe, name = "view_employee"),
    path('clientlogin/',clientslogin, name = "clientlogin"),
    path('employelogin/',employelogins, name = "employelogin"),
    path('employesignup/',employeesignup, name = "employesignup"),
    path('clientsignup/',clients_signup, name = "clientsignup"),
    path('client_view/',client_views, name = "client_view"),
    path('feature/',feature, name = "feature"),
    path('mainn_admin/',admin_homepage, name = "mainn_admin"),
    path('services/',ourservices, name = "services"),
    path('contact/',contact_us, name = "contact"),
    path('booking_view/',booking_views, name = "booking_view"),
    path('hotel_views/',hotel_view, name = "hotel_views"),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('addservice/',addservices, name = "addservice"),
    path('sucess/',sucess_message, name = "sucess"),
    path('credit/',credit_card, name = "credit"),
    path('booking/',booking_view, name = "booking"),
    path('booking_appointments/',booking_appointment, name = "booking_appointments"),
    path('payment_method/',payment_methods, name = "payment_method"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
