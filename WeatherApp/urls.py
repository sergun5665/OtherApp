from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
    path('news/', include('weather.urls')),
    path('certificates/', include('weather.urls')),

]
