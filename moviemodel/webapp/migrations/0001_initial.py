# Generated by Django 3.0.1 on 2020-11-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('moviename', models.CharField(max_length=20)),
                ('hero', models.CharField(max_length=20)),
                ('heroine', models.CharField(max_length=20)),
                ('ratings', models.IntegerField()),
            ],
        ),
    ]
