from django.db.models import Model, DateTimeField
from datetime import datetime


class TimeStampModel(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
