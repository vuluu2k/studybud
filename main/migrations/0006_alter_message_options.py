# Generated by Django 4.1.7 on 2023-03-21 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
