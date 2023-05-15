# Generated by Django 4.1.7 on 2023-04-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performance',
            options={'verbose_name': 'Performance', 'verbose_name_plural': 'Performance'},
        ),
        migrations.AlterField(
            model_name='exercises',
            name='difficulty_level',
            field=models.TextField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('elite', 'Elite')], default='beginner'),
        ),
    ]
