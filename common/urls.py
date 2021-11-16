from django.contrib.auth import views as auth_views
from django.urls import path
from . import views #현재 있는 얘로부터 views를  import한다 

app_name='common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), #login 요청이 들어오면~
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #로그아웃은 그냥 메소드 호출만 하고 종료 
    path('signup/', views.signup, name='signup'),
]
