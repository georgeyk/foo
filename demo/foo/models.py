from django.db import models

from simple_history.models import HistoricalRecords
from charidfield import CharIDField
from ulid import ULID


class Foo(models.Model):
    id = CharIDField(primary_key=True, max_length=32, default=ULID)
    bar = models.CharField(max_length=32, blank=True, default="")
    history = HistoricalRecords()
