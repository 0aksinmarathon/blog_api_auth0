from rest_framework.viewsets import ModelViewSet
from blog.modules.article.models import Article
from blog.modules.article.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
