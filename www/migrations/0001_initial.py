# Generated by Django 2.1.8 on 2019-05-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.URLField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
