# Generated by Django 4.1.5 on 2023-01-20 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emargement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emargement',
            old_name='first_name',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='emargement',
            old_name='last_name',
            new_name='numero_telephone',
        ),
        migrations.RenameField(
            model_name='emargement',
            old_name='phone_number',
            new_name='prenom',
        ),
    ]
