# Generated by Django 2.2.3 on 2019-10-07 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcribe', '0002_transcribe_raw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcribe',
            name='File',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='audio.File'),
        ),
    ]
