# Generated by Django 5.1.2 on 2025-01-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0003_stanowisko_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default='2025-01-18'),
            preserve_default=False,
        ),
    ]
