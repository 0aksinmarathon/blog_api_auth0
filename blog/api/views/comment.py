from rest_framework.viewsets import ModelViewSet
from blog.modules.comment.models import Comment
from blog.modules.comment.serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class CommentViewSet(ModelViewSet):
    renderer_classes = (JSONRenderer,)
    serializer_class = CommentSerializer

    def list(self, request):
        queryset = Comment.objects.all()
        if request.query_params.get('article'):
            queryset = queryset.filter(article=request.query_params.get('article'))

        return Response(CommentSerializer(queryset, many=True).data)
