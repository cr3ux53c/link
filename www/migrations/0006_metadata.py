# Generated by Django 2.1.8 on 2019-05-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_auto_20190505_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.URLField(unique=True, verbose_name='접두 URL')),
            ],
            options={
                'verbose_name': '접두 URL',
                'verbose_name_plural': '접두 URL',
            },
        ),
    ]
