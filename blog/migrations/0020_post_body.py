# Generated by Django 4.1.7 on 2023-03-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
