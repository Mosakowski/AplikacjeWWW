from django.contrib import admin
from .models import Category, Topic, Post

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','category','created')
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    readonly_fields = ('created_at',)
    list_display = ('title','topic','text','slug','created_at','created_by','updated_at')
    list_filter = ('topic__name', 'topic__category__name')

    @admin.display(description='Topic')
    def formatted_topic(self,obj):
        return f"{obj.topic.name} ({obj.topic.category.name})"