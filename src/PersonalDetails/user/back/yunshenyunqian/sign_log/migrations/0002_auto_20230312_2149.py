# Generated by Django 3.2 on 2023-03-12 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_log', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='invitationCodes',
        ),
        migrations.DeleteModel(
            name='logAndsign',
        ),
    ]
