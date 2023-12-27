from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'author', views.CustomerViewSet)
router.register(r'publisher', views.ProductViewSet)
router.register(r'language', views.ProductViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
