from blog.models import Category, Post, Topic, User
from blog.serializers import CategoryCustomSerializer, PostSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

category = Category(name='Sport', description='Kategorie sportowe')
category.save()

category_serializer = CategoryCustomSerializer(category)
content = JSONRenderer().render(category_serializer.data)

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = CategoryCustomSerializer(data=data)
if deserializer.is_valid():
    category_obj = deserializer.save()
else:
    print(deserializer.errors)

user = User.objects.first()
topic = Topic.objects.first()

post = Post(
    title='Pierwszy post',
    text='To jest treść pierwszego posta.',
    topic=topic,
    created_by=user,
    slug='pierwszy-post'
)
post.save()

post_serializer = PostSerializer(post)
post_content = JSONRenderer().render(post_serializer.data)

stream_post = io.BytesIO(post_content)
data_post = JSONParser().parse(stream_post)

post_deserializer = PostSerializer(data=data_post)
if post_deserializer.is_valid():
    post_obj = post_deserializer.save()
else:
    print(post_deserializer.errors)
