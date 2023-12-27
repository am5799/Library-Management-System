from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'author', views.AuthorView)
router.register(r'publisher', views.PublisherView)
router.register(r'language', views.LanguageView)


# The API URLs are now determined automatically by the router
urlpatterns = [
    path('/', include(router.urls)),
]
