import re
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from rest_framework import status, viewsets, generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from uritemplate import partial

from .models import Post
from .serializers import PostSerializer


class PostListMixin(ListModelMixin, CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kargs):
        return self.list(request=request)

    def post(self, request, *args, **kargs):
        self.get_queryset()
        return self.create(request=request)


class PostDetailMixin(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kargs):
        return self.retrieve(request=request)

    def put(self, request, *args, **kargs):
        return self.partial_update(request=request, *args, **kargs)
    
    def delete(self, request, *args, **kargs):
        return self.destroy(request=request, *args, **kargs)




# Create your views here.
# class PostListAPIView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         serializer = PostSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             Response(serializer.data, status=200)
#         else:
#             return Response(serializer.errors, status=400)

# class PostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# post_list = PostViewSet.as_view({
#     'get':'list',
#     'post': 'create'
# })

# post_detail = PostViewSet.as_view({
#     'get':'retrieve',
#     'put': 'update',
#     'patch':'partial_update',
#     'delete':'destory'
# })