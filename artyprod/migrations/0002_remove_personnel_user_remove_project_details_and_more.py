# Generated by Django 4.1.7 on 2023-04-17 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='details',
        ),
        migrations.RemoveField(
            model_name='project',
            name='services',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.DeleteModel(
            name='Personnel',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]