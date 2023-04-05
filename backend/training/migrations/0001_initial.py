# Generated by Django 4.1.7 on 2023-04-05 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('swimmers', '0001_initial'),
        ('administration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(help_text="indicate the category or type of exercise, such as 'strokes,' 'drills,' 'kick sets,' 'pull sets,' etc.", max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Exercise Category',
                'verbose_name_plural': 'Exercise Categories',
            },
        ),
        migrations.CreateModel(
            name='PracticeSessions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('start_at', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='administration.pools')),
                ('squad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='swimmers.squads')),
            ],
            options={
                'verbose_name': 'Practice Session',
                'verbose_name_plural': 'Practice Sessions',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('repetitions', models.IntegerField(default=1)),
                ('duration', models.DurationField()),
                ('distance', models.FloatField(null=True)),
                ('pace', models.IntegerField(null=True)),
                ('intensity', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], max_length=20)),
                ('rest_frequency', models.IntegerField(default=0)),
                ('rest_length_avg', models.DurationField(null=True)),
                ('heart_rate', models.IntegerField(null=True)),
                ('technique', models.TextField(blank=True, default='')),
                ('goal', models.TextField(blank=True, default='')),
                ('feedback', models.TextField(blank=True, default='')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='training.practicesessions')),
                ('swimmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('target_muscle', models.CharField(default='', max_length=50)),
                ('difficulty_level', models.IntegerField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('elite', 'Elite')], default='beginner')),
                ('recommended_duration', models.DurationField(default=None, null=True)),
                ('recommended_repetitions', models.IntegerField(default=1)),
                ('focus_area', models.CharField(default='', max_length=100)),
                ('iframe_video_link', models.URLField(default=None, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.exercisecategories')),
            ],
            options={
                'verbose_name': 'Exercise',
                'verbose_name_plural': 'Exercises',
            },
        ),
        migrations.AddConstraint(
            model_name='exercisecategories',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('category'), name='unique_lower_exercise_category'),
        ),
        migrations.AddConstraint(
            model_name='exercises',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='unique_lower_name_exercise'),
        ),
    ]