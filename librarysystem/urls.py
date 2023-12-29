from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('bookmanagement.urls')),
    path('users/', include('usermanagement.urls')),
]
