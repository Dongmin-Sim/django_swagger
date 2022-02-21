from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import PostViewSet
# from .views import post_list, post_detail
from .views import *

# router = DefaultRouter()
# router.register(r'post', PostViewSet, basename='posts')

urlpatterns = [
    # path('', include(router.urls))
    path('post/', PostListMixin.as_view()),
    path('post/<int:pk>/', PostDetailMixin.as_view())
]