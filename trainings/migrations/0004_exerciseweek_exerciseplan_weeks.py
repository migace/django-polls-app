# Generated by Django 4.2.5 on 2023-10-14 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0003_exerciseplan_remove_exercise_destination_scale_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255, null=True)),
                ('quantity', models.CharField(max_length=255, null=True)),
                ('difficulty', models.CharField(max_length=255, null=True)),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainings.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exerciseplan',
            name='weeks',
            field=models.ManyToManyField(to='trainings.exerciseweek'),
        ),
    ]
