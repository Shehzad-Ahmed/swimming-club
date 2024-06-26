# Generated by Django 4.1.7 on 2023-04-17 18:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_rename_participants_participation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventtypes',
            name='id',
        ),
        migrations.AddField(
            model_name='events',
            name='skill_level',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9, message='Skill level needs to be between 0 to 9')]),
        ),
        migrations.AlterField(
            model_name='eventtypes',
            name='type',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('attended', models.BooleanField(default=True)),
                ('score', models.FloatField(default=0)),
                ('position', models.PositiveIntegerField(default=0)),
                ('record', models.TextField()),
                ('participation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.participation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
