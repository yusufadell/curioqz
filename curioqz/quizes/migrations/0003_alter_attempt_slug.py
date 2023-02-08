# Generated by Django 4.0.8 on 2023-02-06 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='slug',
            field=models.SlugField(default=uuid.UUID('85cc53ea-1b08-4aad-a652-cb5df8178bb4'), unique=True),
        ),
    ]