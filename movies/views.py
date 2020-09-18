from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.urls import reverse_lazy

from rest_framework.response import Response
import datetime
from rest_framework import viewsets
import json
from movies.models import Movie
from rest_framework import permissions

from rest_framework.exceptions import APIException

from django.core import serializers
from movies.serializers import MovieSerializer
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Movie.objects.all()  # .order_by("-rating")
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "year"]

    # Cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, format=None):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

