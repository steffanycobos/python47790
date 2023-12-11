# Generated by Django 4.2.7 on 2023-11-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=15)),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Familia',
        ),
    ]
