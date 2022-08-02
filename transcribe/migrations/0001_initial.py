# Generated by Django 2.2.3 on 2019-10-07 00:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('audio', '0007_auto_20191003_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_text', models.TextField(default='')),
                ('enthusiasm_text', models.TextField(default='')),
                ('focus_text', models.TextField(default='')),
                ('imagine_text', models.TextField(default='')),
                ('integrity_text', models.TextField(default='')),
                ('smart_text', models.TextField(default='')),
                ('solid_text', models.TextField(default='')),
                ('speed_text', models.TextField(default='')),
                ('totality_text', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('File', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='audio.File')),
            ],
        ),
    ]