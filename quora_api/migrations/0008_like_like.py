# Generated by Django 2.2.5 on 2019-10-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora_api', '0007_auto_20191007_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]