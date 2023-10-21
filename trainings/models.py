from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    execution = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255, null=True)
    image_link = models.CharField(max_length=255, null=True)
    tips = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name


class ExerciseWeek(models.Model):
    DIFFICULTY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    name = models.CharField(max_length=255)
    exercise = models.ForeignKey('Exercise', on_delete=models.SET_NULL, null=True)
    weight = models.CharField(max_length=255, null=True)
    quantity = models.CharField(max_length=255, null=True)
    difficulty = models.CharField(max_length=255, choices=DIFFICULTY_CHOICES, null=True)


class ExercisePlan(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.SET_NULL, null=True)
    destination_scale = models.CharField(max_length=255, null=True)
    volume = models.CharField(max_length=255, null=True)
    weeks = models.ManyToManyField(ExerciseWeek)

    def __str__(self):
        return self.exercise.name + " (" + self.destination_scale + ", " + self.volume + ")";


class TrainingPlan(models.Model):
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(ExercisePlan)
