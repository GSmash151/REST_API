
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
    
    # Web Application Endpoint
    path('admin/', admin.site.urls), 

    # API Endpoints
    path('api/v1/', include('api.urls'))   
]
