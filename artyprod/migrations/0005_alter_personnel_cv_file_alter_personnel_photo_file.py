# Generated by Django 4.1.7 on 2023-04-17 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0004_alter_personnel_cv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='cv_file',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='photo_file',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
