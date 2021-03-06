# Generated by Django 2.1.8 on 2019-05-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '링크', 'verbose_name_plural': '링크'},
        ),
        migrations.RemoveField(
            model_name='link',
            name='text',
        ),
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='link',
            name='href',
            field=models.URLField(verbose_name='링크'),
        ),
    ]
