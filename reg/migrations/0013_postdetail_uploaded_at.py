# Generated by Django 4.0.3 on 2022-03-28 08:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0012_delete_posthome'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdetail',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
