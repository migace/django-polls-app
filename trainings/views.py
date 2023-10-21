from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from trainings.models import Exercise, TrainingPlan
from trainings.serializers import ExerciseSerializer, TrainingPlanSerializer


class ExerciseViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
            List all the Exercise items
        '''
        querySet = Exercise.objects.all()
        serializer = ExerciseSerializer(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Exercise with given exercise data
        '''
        data = {
            'name': request.data.get('name'),
            'execution': request.data.get('execution'),
            'video_link': request.data.get('video_link') or None,
            'image_link': request.data.get('image_link') or None,
            'tips': request.data.get('tips'),
        }
        serializer = ExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseDetailsViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, exercise_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Exercise.objects.get(id=exercise_id)
        except Exercise.DoesNotExist:
            return None

    def get(self, request, exercise_id):
        '''
        Retrieves the Exercise with given exercise_id
        '''
        exercise_instance = self.get_object(exercise_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ExerciseSerializer(exercise_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, exercise_id):
        '''
        Updates the exercise item with given exercise_id if exists
        '''
        exercise_instance = self.get_object(exercise_id)
        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name', exercise_instance.name),
            'execution': request.data.get('execution', exercise_instance.execution),
            'video_link': request.data.get('video_link', exercise_instance.video_link),
            'image_link': request.data.get('image_link', exercise_instance.image_link),
            'tips': request.data.get('tips', exercise_instance.tips),
            'is_active': request.data.get('is_active', exercise_instance.is_active)
        }
        serializer = ExerciseSerializer(instance=exercise_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, exercise_id):
        '''
        Delete the Exercise with given id
        '''
        exercise_instance = self.get_object(exercise_id)

        if not exercise_instance:
            return Response(
                {"res": "Object with exercise id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        exercise_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class TrainingPlanViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        querySet = TrainingPlan.objects.all()
        serializer = TrainingPlanSerializer(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
