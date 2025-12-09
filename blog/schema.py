import graphene
from graphene_django import DjangoObjectType
from posts.models import Topic, Category, Post


# dzięki wykorzystaniu klasy DjangoObjectType możemy w łatwy sposób
# wskazać klasę wcześniej zdefiniowanego modelu, która zostanie wykorzystana
# w schemie GraphQL umożliwiając połączenie Django QuerySet oraz zapytań
# poprzez GraphQL. Podobnie jak w przypadku definicji własności w klasach
# administracyjnych danego modelu (plik admin.py) tutaj też możemy określić
# np. listę pól, które poprzez GraphQL chcemy wystawić z danego modelu
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"

class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
        fields = "__all__"

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, text):
        post = Post(title=title, text=text)
        post.save()
        return CreatePost()


class UpdatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        test = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info,title=None, text=None):
        post = Post.objects.get(title = title)

        if title is not None:
            post.title = title
        if text is not None:
            post.text = text

        post.save()
        return UpdatePost()


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()


# klasa Query pozwala określić pola (tu np. all_teams, person_by_id, itd.)
# które są dostępne, a następnie Resolvery, który definiują w jaki sposób
# dane dla wskazanego pola będą pobierane (tu już używamy znany nam
# sposób z użyciem Django QuerySet)

class Query(graphene.ObjectType):
    # typ graphene.List określa, że zwracana będzie lista obiektów danego typu
    all_topics = graphene.List(TopicType)

    # tu określamy, że zwrócony będzie obiekt typu PersonType, a jego wyszukanie
    # odbędzie się na podstawie jego atrybutu id o typie Int, który jest wymagany
    category_by_id = graphene.Field(CategoryType, id=graphene.Int(required=True))

    all_posts = graphene.List(PostType)
    post_by_title = graphene.Field(PostType, title=graphene.String(required=True))

    # resolver dla pola all_teams
    # root główny obiekt wartości przekazywany przez zapytanie
    # info informacje z resolvera
    # args słownik (opcjonalnie), parametrów przekazywanych do resolvera
    def resolve_all_topics(root, info):
        return Topic.objects.all()

    def resolve_category_by_id(root, info, id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            raise Exception('Invalid category Id')

    def resolve_all_posts(root, info):
        return Post.objects.all()

    def resolve_post_by_name(root, info, title):
        try:
            return Post.objects.get(title=title)
        except Post.DoesNotExist:
            raise Exception(f'No post with name \'{title}\' found.')

    def resole_find_topics_by_phrase(self, info, phrase):
        return Topic.objects.filter(name__icontains=phrase)


schema = graphene.Schema(query=Query)