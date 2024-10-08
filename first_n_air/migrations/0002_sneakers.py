# Generated by Django 5.1 on 2024-08-30 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_n_air', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('character', models.TextField()),
                ('price_type', models.CharField(choices=[("so'm", "so'm"), ('₽', '₽'), ('$', '$')], default="so'm", max_length=10)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_n_air.category')),
            ],
        ),
    ]
