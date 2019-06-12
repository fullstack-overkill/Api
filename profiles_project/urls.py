from django.contrib import admin as admin_django
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path('admin/', admin_django.site.urls),
    path('api/', include('profiles_api.urls')),
]
