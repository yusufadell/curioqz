from django.contrib.auth import get_user_model
from rest_framework import serializers

from curioqz.courses.api.serializers import CourseSerializer
from curioqz.questions.api.serializers import QuestionSerializer
from curioqz.quizes.models import Attempt
from curioqz.quizes.models import Grade
from curioqz.quizes.models import Quiz
from curioqz.quizes.models import QuizGrade
from curioqz.quizes.models import QuizQuestion
from curioqz.quizes.models import Review

User = get_user_model()


class QuizSerializer(serializers.ModelSerializer):
    """ """
    course_obj = CourseSerializer(source="course", read_only=True)

    class Meta:
        """ """
        model = Quiz
        fields = "__all__"


class QuizGradeSerializer(serializers.Serializer):
    """ """
    url = serializers.CharField(source="grade.grade", read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    quiz_obj = QuizSerializer(source="quiz", read_only=True)

    class Meta:
        """ """
        model = QuizGrade
        fields = "__all__"


class QuizQuestionSerializer(serializers.ModelSerializer):
    """ """
    quiz_obj = QuizSerializer(
        source="quiz", read_only=True
    )  # TODO: use drf writalbe nested
    question_obj = QuestionSerializer(
        source="question", read_only=True
    )  # TODO: consider using django-auto-prefetching pkg

    class Meta:
        """ """
        model = QuizQuestion
        fields = "__all__"


class ReviewSerializer: ...


class AttemptSerializer: ...


class GradeSerializer: ...
