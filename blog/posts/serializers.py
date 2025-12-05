from rest_framework import serializers
from .models import Category, Topic, Post
import datetime


class CategorySerializer(serializers.Serializer):

    name = serializers.CharField(max_length=60)
    description = serializers.CharField(default="brak")

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance



class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name', 'category', 'created']

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'topic', 'slug', 'created_at', 'updated_at', 'created_by']

        def validate_name(self, value):
            if not value.istitle():
                raise serializers.ValidationError("Nazwa osoby powinna zaczac sie wielka litera")
            return value

        def validate_creation_date(self, value):
            if value > datetime.datetime.now():
                raise serializers.ValidationError("data z przyszlosci")
            return value

