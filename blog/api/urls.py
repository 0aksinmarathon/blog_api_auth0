from rest_framework.routers import DefaultRouter
from .views.article import ArticleViewSet
from .views.comment import CommentViewSet
from .views.user import UserViewSet

router = DefaultRouter(trailing_slash=False)

router.register(
    r'article',
    ArticleViewSet,
    basename='article'
)

router.register(
    r'comment',
    CommentViewSet,
    basename='comment'
)

router.register(
    r'user',
    UserViewSet,
    basename='user'
)

urlpatterns = router.urls
