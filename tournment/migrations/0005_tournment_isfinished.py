# Generated by Django 5.1.5 on 2025-01-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournment', '0004_remove_playermatch_date_alter_tournment_clan1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournment',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
    ]
