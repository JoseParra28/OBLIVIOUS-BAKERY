# Generated by Django 3.1 on 2023-04-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20230405_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
