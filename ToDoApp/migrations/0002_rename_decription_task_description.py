# Generated by Django 3.2.5 on 2021-08-01 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='decription',
            new_name='description',
        ),
    ]
