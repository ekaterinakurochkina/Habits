from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import (HabitpublicityListAPIView, HabitViewSet,
                         UserhabitListAPIView)

app_name = HabitsConfig.name

router = SimpleRouter()
router.register("", HabitViewSet)

urlpatterns = [
    path("habitpublicity/", HabitpublicityListAPIView.as_view(), name="habitpublicity"),
    path("userhabit/", UserhabitListAPIView.as_view(), name="userhabit"),
]

urlpatterns += router.urls
