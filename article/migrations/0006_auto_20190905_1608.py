# Generated by Django 2.2.4 on 2019-09-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20190905_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=50, verbose_name='İsim'),
        ),
    ]
