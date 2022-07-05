from django.urls import path, include
from . import views


urlpatterns = [

    # path('profile/update/plate', include('main.urls')),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile_page'),
    path('profile/update/<int:pk>', views.ProfileUpdate.as_view(), name='update_profile_page'),



]