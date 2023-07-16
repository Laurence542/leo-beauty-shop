# Generated by Django 4.2.2 on 2023-07-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_client_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_signups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_full_name', models.CharField(max_length=255)),
                ('employee_email', models.EmailField(max_length=255)),
                ('employee_password', models.CharField(max_length=255)),
            ],
        ),
    ]
