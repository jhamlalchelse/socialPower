from django.urls import path
from reg import views
from django.contrib.auth import views as auth_views
from .forms import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    # path('registration/', views.CustomerRegistrationView.as_view(), name='registration'),
    path('account/login/', auth_views.LoginView.as_view(template_name="login.html",authentication_form=LoginForm), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('myprofile/',views.ProfileView.as_view(), name='myprofile'),
    path('userpost/<int:pk>',views.userpost, name='userpost'),
    path('userpostdetail/<int:pk>',views.userpostdetail, name='userpostdetail'),
    path('mypost/',views.mypost, name='mypost'),
    path('mypostdetail/<int:pk>',views.mypostdetail, name='mypostdetail'),
    path('userprofile/<int:pk>',views.userprofile, name='userprofile'),
    path('follow/<int:pk>',views.follow, name='follow'),
    path('follow/<int:userfwid>/<int:pk>',views.follow, name='follow'),
    path('unfollow/<int:pk>',views.unfollow, name='unfollow'),
    path('unfollow/<int:userfwid>/<int:pk>',views.unfollow, name='unfollow'),
    path('follower/',views.follower, name='follower'),
    path('follower/<int:pk>',views.follower, name='follower'),
    path('following/',views.following, name='following'),
    path('following/<int:pk>',views.following, name='following'),
    path('deletefolloweruser/<int:userfwid>/<int:pk>',views.deletefolloweruser, name='deletefolloweruser'),
    path('searchuser/',views.searchuser, name='searchuser'),
    path('searchfollow/<int:userfwid>/<int:pk>',views.searchfollow, name='searchfollow'),
    path('userfollower/<int:pk>',views.userfollower, name='userfollower'),
    path('userfollowing/<int:pk>',views.userfollowing, name='userfollowing'),
    path('userfollow/<int:userfwid>/<int:pk>',views.userfollow, name='userfollow'),
    path('userunfollow/<int:userfwid>/<int:pk>',views.userunfollow, name='userunfollow'),
    path('userfollowinfollower/<int:userfwid>/<int:pk>',views.userfollowinfollower, name='userfollowinfollower'),
    path('userunfollowinfollower/<int:userfwid>/<int:pk>',views.userunfollowinfollower, name='userunfollowinfollower'),
    path('addpost/',views.addpost, name='addpost'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)