# Generated by Django 2.0 on 2017-12-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20171220_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplex',
            name='maiormenorR3',
            field=models.CharField(choices=[('>=', '>='), ('=', '='), ('<=', '=>')], default='>=', max_length=10),
        ),
    ]