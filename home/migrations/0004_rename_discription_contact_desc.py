# Generated by Django 4.1.1 on 2023-03-25 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Discription',
            new_name='desc',
        ),
    ]