from rest_framework import serializers
from .models import Exercise, TrainingPlan, ExercisePlan, ExerciseWeek


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class ExerciseWeekSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False, read_only=True)

    class Meta:
        model = ExerciseWeek
        fields = '__all__'


class ExercisePlanSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False, read_only=True)
    weeks = ExerciseWeekSerializer(many=True, read_only=True)

    class Meta:
        model = ExercisePlan
        fields = '__all__'


class TrainingPlanSerializer(serializers.ModelSerializer):
    exercises = ExercisePlanSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingPlan
        fields = '__all__'
