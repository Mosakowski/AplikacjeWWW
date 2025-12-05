from posts.models import Category, Topic
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from posts.serializers import TopicModelSerializer, CategorySerializer
    
category = Category(name= 'newsy', description = 'informacje roznego rodzaju')
category.save()

serializer = CategorySerializer(category)
serializer.data

content = JSONRenderer().render(serializer.data)
content

topic = Topic(name = 'nazwa topika', category = category, created = '')

topic.save()

serializer = TopicModelSerializer(topic)
serializer.data

content = JSONRenderer().render(serializer.data)
content