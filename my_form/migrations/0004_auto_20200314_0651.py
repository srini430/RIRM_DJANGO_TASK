# Generated by Django 3.0.2 on 2020-03-14 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_form', '0003_auto_20200314_0614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name_plural': 'clients'},
        ),
        migrations.RenameField(
            model_name='clientdetail',
            old_name='first_name',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='clientdetail',
            old_name='last_name',
            new_name='full_name',
        ),
    ]
