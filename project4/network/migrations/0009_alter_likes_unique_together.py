# Generated by Django 4.2.3 on 2023-07-11 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_alter_follow_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='likes',
            unique_together={('liker', 'post')},
        ),
    ]
