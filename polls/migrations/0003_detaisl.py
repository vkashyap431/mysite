# Generated by Django 3.0.2 on 2020-01-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200124_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detaisl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
    ]