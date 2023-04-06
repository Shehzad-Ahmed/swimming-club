# Generated by Django 4.1.7 on 2023-04-05 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participants',
            new_name='Participation',
        ),
        migrations.AddField(
            model_name='events',
            name='participants',
            field=models.ManyToManyField(through='competitions.Participation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.events'),
        ),
    ]
