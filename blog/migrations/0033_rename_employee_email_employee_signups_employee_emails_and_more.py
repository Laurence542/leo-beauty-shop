# Generated by Django 4.2.2 on 2023-07-11 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_client_signup_client_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_signups',
            old_name='employee_email',
            new_name='employee_emails',
        ),
        migrations.RenameField(
            model_name='employee_signups',
            old_name='employee_full_name',
            new_name='employee_full_names',
        ),
        migrations.RenameField(
            model_name='employee_signups',
            old_name='employee_password',
            new_name='employee_passwords',
        ),
    ]
