# Generated by Django 3.0.2 on 2020-03-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itoneapp', '0004_auto_20200316_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotion',
            name='color',
            field=models.CharField(default='#202020', max_length=20),
            preserve_default=False,
        ),
    ]