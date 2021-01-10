from rest_framework import serializers
from blog.modules.article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'body']

