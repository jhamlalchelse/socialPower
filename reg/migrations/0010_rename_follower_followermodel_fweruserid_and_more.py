# Generated by Django 4.0.3 on 2022-03-24 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0009_followingmodel_followermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followermodel',
            old_name='follower',
            new_name='fweruserid',
        ),
        migrations.RenameField(
            model_name='followingmodel',
            old_name='following',
            new_name='fwinguserid',
        ),
    ]
