# Generated by Django 5.1.4 on 2025-02-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='attachfile',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
