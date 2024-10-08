from django.urls import path,include
from profiles_api import views
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet, basename='profile')
router.register('feed', views.UserProfileFeedViewSet, basename='feed')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),  # Include the login URL in the main URLconf
    path('', include(router.urls)),  # Include the router URLs in the main URLconf


]
