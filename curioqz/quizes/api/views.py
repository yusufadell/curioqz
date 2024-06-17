import pysnooper
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from curioqz.quizes.api.serializers import QuizGradeSerializer
from curioqz.quizes.api.serializers import QuizQuestionSerializer
from curioqz.quizes.api.serializers import QuizSerializer
from curioqz.quizes.models import Attempt
from curioqz.quizes.models import Grade
from curioqz.quizes.models import Quiz
from curioqz.quizes.models import QuizGrade
from curioqz.quizes.models import QuizQuestion
from curioqz.quizes.models import Review


@pysnooper.snoop()
class QuizViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ """
    queryset = (Quiz.objects.select_related(
        "course", "course__owner",
        "review").prefetch_related("course__modules").all())
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        """

        :param request:
        :param *args:
        :param **kwargs:

        """
        print(self)
        print(vars(self))
        return Response("Hello")

    @action(
        methods=["get"],
        detail=False,
        url_path="lol",
        name="Fuck",
    )
    def yusuf_was_here(self, request, *args, **kwargs):
        """The latest DRF includes self.request in the default context sent to serializers;
        you don't need to manually add it in.
        previosly it was: self.context['request'].user

        :param request:
        :param *args:
        :param **kwargs:

        """
        from pprint import pprint

        print(args, kwargs)
        pprint(self.request.query_params)
        pprint(self.request.data)
        pprint(vars(self))
        lol = self.get_object()
        pprint(lol)

        # pprint(self.get_queryset())
        # qs = self.get_queryset()
        # return Response(
        #     self.get_serializer(qs.get(pk=self.request.query_params.get("id"))).data
        # )
        return Response("Hello")

    # @yusuf_was_here.mapping.get
    # def create_example(self, request, **kwargs):
    #     lol = self.get_object()
    #     return Response(self.get_serializer(lol).data)


class QuizGradeViewSet(viewsets.ModelViewSet):
    """ """
    queryset = QuizGrade.objects.all()
    serializer_class = QuizGradeSerializer


class QuizQuestionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ """
    queryset = (QuizQuestion.objects.select_related("quiz").prefetch_related(
        "quiz__course__modules").all())
    serializer_class = QuizQuestionSerializer
