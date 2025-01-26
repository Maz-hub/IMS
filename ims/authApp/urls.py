from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login"),  # Login page
    path('logout/', views.logout_view, name="logout"),  # Logout page
    path('register/', views.register_view, name="register"),  # Register page
    path('protected/', views.ProtectedView.as_view(), name="protected"),  # Protected page
]
