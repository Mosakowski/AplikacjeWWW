from django.urls import path, include
from rest_framework.decorators import api_view
from . import api_views

urlpatterns = [
    path('topic/list', api_views.topic_list),
    path('topic/<int>:pk', api_views.topic_view),
    path('topic/add', api_views.topic_add),
    path('topic/delete/<int:pk>/', api_views.topic_delete),
    path('topic/list_with_name/search', api_views.topic_list_with_name),

    path('category/list', api_views.category_list),
    path('category/<int>:pk', api_views.category_view),
    path('category/add', api_views.category_add),
    path('category/delete/<int:pk>/', api_views.category_delete),
    path('category/list_with_name/search', api_views.category_list_with_name),

    path('post/<int:pk>', api_views.post_view),
    path('post/add/', api_views.post_add),
    path('post/delete/<int:pk>', api_views.post_delete),
    path('post/search', api_views.post_list),
]