# Generated by Django 4.2.7 on 2024-01-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
