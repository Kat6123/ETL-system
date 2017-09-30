# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Jobs


def index(request, location):
    jobs_in_location = Jobs.objects.filter(location=location).values_list(
        'job_title', 'category', 'status', 'location')
    return HttpResponse(
        "\n".join((", ".join(job) for job in jobs_in_location))
    )
