# Generated by Django 2.0.6 on 2018-10-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20181015_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbook',
            name='content',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='guestbook',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='guestbook',
            name='reg_date',
            field=models.DateTimeField(default='2018-10-15 10:00:00'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
