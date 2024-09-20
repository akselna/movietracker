# Generated by Django 5.0.1 on 2024-02-13 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_actor_favorite_genre_review_series_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='rating_range',
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('rating__gte', 1), ('rating__lte', 5)), ('rating__isnull', True), _connector='OR'), name='rating_range'),
        ),
    ]
