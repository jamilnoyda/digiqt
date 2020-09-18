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


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Movie.objects.all().order_by("-rating")
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.serializer_class(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)

    #     today = datetime.date.today()

    #     todays_records = Movie.objects.filter(updated_at__gt=today)[:10]
    #     if todays_records.count() > 10:
    #         raise APIException("today limit reached")

    #     serializer.save()
    #     return Response(serializer.data)

