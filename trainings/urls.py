from django.urls import path
from .views import (
    ExerciseViewSet,
    ExerciseDetailsViewSet,
    TrainingPlanViewSet
)

urlpatterns = [
    path('api/exercises', ExerciseViewSet.as_view()),
    path('api/exercises/<int:exercise_id>', ExerciseDetailsViewSet.as_view()),
    path('api/training-plans', TrainingPlanViewSet.as_view({'get': 'list'}))
]
