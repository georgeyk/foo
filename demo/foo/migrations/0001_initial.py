# Generated by Django 4.2.5 on 2023-09-05 01:20

import charidfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import ulid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Foo",
            fields=[
                (
                    "id",
                    charidfield.fields.CharIDField(
                        default=ulid.ULID,
                        max_length=32,
                        prefix="",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("bar", models.CharField(blank=True, default="", max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalFoo",
            fields=[
                (
                    "id",
                    charidfield.fields.CharIDField(
                        db_index=True,
                        default=ulid.ULID,
                        max_length=32,
                        prefix="",
                        unique=True,
                    ),
                ),
                ("bar", models.CharField(blank=True, default="", max_length=32)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical foo",
                "verbose_name_plural": "historical foos",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
