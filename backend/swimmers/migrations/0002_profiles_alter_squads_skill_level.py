# Generated by Django 4.1.7 on 2023-04-06 16:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_users_managers_users_date_of_birth'),
        ('swimmers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('skill_level', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9, message='Skill level needs to be between 0 to 9')])),
                ('badge', models.CharField(blank=True, default='', max_length=50)),
                ('overall_score', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='squads',
            name='skill_level',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9, message='Skill level needs to be between 0 to 9')]),
        ),
    ]
