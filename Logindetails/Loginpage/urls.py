from django.urls import path
from . import views

urlpatterns = [
    # path('',views.user_sign_built,name='signup'),
    # path('login/',views.user_login,name='login'),
    # path('profile/',views.user_profile,name='profile'),
    # path('logout/',views.user_logout,name='logout'),
    path('login',views.login_us,name = 'login'),
    path('',views.sign_up,name = 'signup'),
]
