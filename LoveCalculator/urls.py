from django.contrib import admin
from django.urls import path
# IMPORTANT: Replace 'YOUR_APP_NAME' with your actual app folder name (e.g., calculator)
from LoveCalculator import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # This points the homepage directly to your view
]