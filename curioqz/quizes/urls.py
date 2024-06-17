from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from curioqz.quizes.api.views import QuizGradeViewSet
from curioqz.quizes.api.views import QuizQuestionViewSet
from curioqz.quizes.api.views import QuizViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("quizes", QuizViewSet)
router.register("quiz-grades", QuizGradeViewSet)  # make as detailed endpoint for grades
router.register("quiz-questions", QuizQuestionViewSet)

app_name = "quizes"
urlpatterns = router.urls
