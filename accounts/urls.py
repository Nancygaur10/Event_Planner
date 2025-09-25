from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('admin/dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('user/dashboard/',views.user_dashboard,name='user_dashboard'),
]