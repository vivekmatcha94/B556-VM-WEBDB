
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('Vivekweb/', include('Vivekweb.urls')),
    path('admin/', admin.site.urls),
]

