# Generated by Django 2.1.5 on 2019-01-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailValid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
                ('email_address', models.EmailField(max_length=254)),
                ('times', models.DateTimeField()),
            ],
        ),
    ]
