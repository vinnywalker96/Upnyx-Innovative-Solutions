from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView
from  . import views

urlpatterns = [
	path('user/signup', views.UserSignUpView.as_view(), name='user-signup'),
	path('user/login', views.UserLoginView.as_view(), name='user-login'),
	path('token_balance', views.TokenBalanceView.as_view(), name='token balance'),
	path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
	path('chat/', views.ChatAPIView.as_view(), name='chat'),
 ]