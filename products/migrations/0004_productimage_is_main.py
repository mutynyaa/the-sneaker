# Generated by Django 3.0.4 on 2020-04-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200402_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]