# Generated by Django 2.1.1 on 2018-09-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='img',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题', max_length=20),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='介绍', max_length=100),
        ),
    ]