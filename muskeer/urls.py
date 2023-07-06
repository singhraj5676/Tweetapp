from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update/',views.update_user, name='update'),
    path('meep_like/<int:pk>',views.meep_like, name='meep_like' ),
    path('meep_show/<int:pk>', views.meep_show, name='meep_show'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('delete_meep/<int:pk>', views.delete_meep, name='delete_meep'),
    path('edit_meep/<int:pk>', views.edit_meep, name='edit_meep'),


]
