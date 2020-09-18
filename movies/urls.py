from django.urls import include, path
from rest_framework import routers


from movies.views import MovieViewSet


router = routers.DefaultRouter()
router.register(r"movies-api", MovieViewSet)

app_name = "movies"
urlpatterns = [
    path("", include(router.urls,)),
]
