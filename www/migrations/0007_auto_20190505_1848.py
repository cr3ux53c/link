# Generated by Django 2.1.8 on 2019-05-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_metadata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metadata',
            options={'verbose_name': '단축 링크 접두 URL', 'verbose_name_plural': '단축 링크 접두 URL'},
        ),
        migrations.AddField(
            model_name='link',
            name='protocol',
            field=models.CharField(default='http://', max_length=20, verbose_name='프로토콜'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='path',
            field=models.CharField(max_length=50, unique=True, verbose_name='단축 경로'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='prefix',
            field=models.URLField(unique=True, verbose_name='단축 링크 접두 URL'),
        ),
    ]