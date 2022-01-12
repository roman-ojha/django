# Generated by Django 2.2 on 2022-01-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
