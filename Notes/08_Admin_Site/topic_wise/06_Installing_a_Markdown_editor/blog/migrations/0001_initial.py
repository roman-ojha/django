# Generated by Django 4.2.1 on 2023-05-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='This is title title', max_length=250)),
                ('content', models.TextField()),
            ],
        ),
    ]
