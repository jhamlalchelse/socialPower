# Generated by Django 4.0.3 on 2022-03-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0010_rename_follower_followermodel_fweruserid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followermodel',
            name='fweruserid',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='followingmodel',
            name='fwinguserid',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
