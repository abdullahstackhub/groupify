# Generated by Django 5.1.4 on 2025-02-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_messages_edit'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntrestNotifition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.JSONField(max_length=500)),
                ('users_recived', models.JSONField(max_length=500)),
            ],
        ),
    ]
