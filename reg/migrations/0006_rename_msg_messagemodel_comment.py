# Generated by Django 4.0.3 on 2022-03-24 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0005_messagemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagemodel',
            old_name='msg',
            new_name='comment',
        ),
    ]
