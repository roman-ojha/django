# Generated by Django 4.2.1 on 2023-05-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_person2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(choices=[('RD', 'Red'), ('BL', 'Blue')], max_length=50)),
            ],
        ),
    ]
