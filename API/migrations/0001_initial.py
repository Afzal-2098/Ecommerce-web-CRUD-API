# Generated by Django 4.0.5 on 2022-06-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('date', models.DateField()),
            ],
        ),
    ]
