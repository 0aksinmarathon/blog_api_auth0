from django.db.models import BigAutoField, ForeignKey, TextField, CASCADE
from blog.modules.user.models import User
from blog.modules.article.models import Article
from ...common.models.timestamp import TimeStampModel


class Comment(TimeStampModel):
    class Meta:
        db_table = 'comments'

    id = BigAutoField(primary_key=True)
    user = ForeignKey(User, on_delete=CASCADE)
    article = ForeignKey(Article, on_delete=CASCADE)
    body = TextField()
