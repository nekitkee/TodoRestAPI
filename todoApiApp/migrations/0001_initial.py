# Generated by Django 2.2.4 on 2019-08-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1024, verbose_name='body')),
                ('date', models.DateField(verbose_name='date')),
            ],
        ),
    ]