# Generated by Django 3.2.4 on 2021-06-24 23:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lecture', '0010_alter_lecture_enrol_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='like_users',
            field=models.ManyToManyField(related_name='like_lectures', to=settings.AUTH_USER_MODEL),
        ),
    ]