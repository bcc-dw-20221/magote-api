# Generated by Django 4.1 on 2022-09-01 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("boteco", "0002_perfil_magote"),
    ]

    operations = [
        migrations.AddField(
            model_name="postagem",
            name="autor",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="postagem",
            name="curtidas",
            field=models.ManyToManyField(
                related_name="curtidas_postagem", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Comentario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("texto", models.CharField(max_length=140)),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "curtidas",
                    models.ManyToManyField(
                        related_name="curtidas_comentarios", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="postagem",
            name="comentarios",
            field=models.ManyToManyField(
                related_name="postagem", to="boteco.comentario"
            ),
        ),
    ]
