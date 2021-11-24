# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from blog.models import Category,Article
from blog.serializers import CategorySerializer,ArticleSerializer, UserSerializers

# Create your views here.
class  UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()