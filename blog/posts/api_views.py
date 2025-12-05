from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Post, Topic
from .serializers import PostModelSerializer, CategorySerializer, TopicModelSerializer
import datetime

@api_view(['GET'])
def topic_view(request, pk):
    topic = Topic.objects.get(name=pk)
    serializer = TopicModelSerializer(topic)
    return Response(serializer.data)

@api_view(['POST'])
def topic_add(request, data):
    topic = Topic.objects.create(name=data['title'], category=data['category'], created=datetime.datetime.now())
    serializer = TopicModelSerializer(topic)
    return Response(serializer.data)

@api_view(['DELETE'])
def topic_delete(request, pk):
    topic = Topic.objects.get(name=pk)
    topic.delete()
    serializer = TopicModelSerializer(topic)
    return Response(serializer.data)

@api_view(['GET'])
def topic_list(request):
    topics = Topic.objects.all()
    serializer = TopicModelSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def topic_list_with_name(request):
    search = request.GET.get('search', '')

    topics = Topic.objects.filter(name__icontains=search)

    serializer = TopicModelSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_view(request, pk):
    category = Category.objects.get(name=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['POST'])
def category_add(request, data):
    category = Category.objects.create(name=data['name'], description=data['description'])
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['DELETE'])
def category_delete(request, pk):
    category = Category.objects.get(name=pk)
    category.delete()
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_list_with_name(request):
    search = request.GET.get('search', '')
    categories = Category.objects.filter(name__icontains=search)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

class PostView(APIView):
    def get(self,request,pk):
        post = Post.objects.get(title=pk)
        serializer = PostModelSerializer(post)
        return Response(serializer.data)

class PostAdd(APIView):
    def add(self,request,data):
        post = Post.objects.create(title=data['title'], text=data['text'], topic=data['topic'], slug=data['slug'],
                                   created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(),
                                   created_by=data['created_by'])
        serializer = PostModelSerializer(post)
        return Response(serializer.data)


class PostDelete(APIView):
    def delete(self,request,pk):
        post = Post.objects.get(title=pk)
        post.delete()
        serializer = PostModelSerializer(post)
        return Response(serializer.data)

class PostList(APIView):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)