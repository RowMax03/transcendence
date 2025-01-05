from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect, name='root_redirect'),  # Root route redirection
    path('signin/', views.signin, name='signin'),  # Sign-in view
	path('signout/', views.signout, name='signout'),  # Sign-out view
    path('oauth_callback/', views.oauth_callback, name='oauth_callback'),  # OAuth callback view

    # If the user is not authenticated, they will be redirected to the sign-in page.
    path('home/', views.home, name='home'),  # Main home view
    path('home/stats/', views.stats, name='stats'),  # Stats view
	path('home/friends/', views.friends, name='friends'),  # Friends view
    path('home/game/', views.game, name='game'),  # Game view
    path('home/profile/', views.profile, name='profile'),  # Profile view
    path('home/chat/', views.chat, name='chat'),  # chat view

]
