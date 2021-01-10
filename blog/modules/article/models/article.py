from django.db.models import BigAutoField, ForeignKey, TextField, CASCADE
from blog.modules.user.models import User
from ...common.models.timestamp import TimeStampModel


class Article(TimeStampModel):
    class Meta:
        db_table = 'articles'

    id = BigAutoField(primary_key=True)
    user = ForeignKey(User, on_delete=CASCADE)
    title = TextField()
    body = TextField()
