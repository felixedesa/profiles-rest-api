# Generated by Django 5.1.1 on 2024-09-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user',
            new_name='user_profile',
        ),
        migrations.AlterField(
            model_name='profilefeeditem',
            name='status_text',
            field=models.CharField(max_length=255),
        ),
    ]
