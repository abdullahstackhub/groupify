# Generated by Django 5.1.4 on 2025-02-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_user_intrest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='intrest',
            field=models.JSONField(max_length=300, null=True),
        ),
    ]
