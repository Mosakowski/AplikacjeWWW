from posts.models import Category, Topic, Post

Category.objects.get(id=3)

Category.objects.filter(name__startswith="A")

Topic.objects.values_list('category__name', flat=True).distinct()

Post.objects.values_list('title', flat=True).order_by('-title')

nowa_kategoria = Category(name="nowa kategoria", description="testowe z shella")
nowa_kategoria.save()
