# Generated by Django 3.1 on 2023-03-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price_m', models.CharField(max_length=5)),
                ('price_l', models.CharField(max_length=5)),
                ('p_image', models.URLField()),
            ],
        ),
    ]
