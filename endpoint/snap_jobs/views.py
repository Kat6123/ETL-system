# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Jobs


def index(request, location):
    if not location:
        jobs_in_location = Jobs.objects.all()
    else:
        jobs_in_location = Jobs.objects.filter(location=location)

    values = jobs_in_location.values_list(
        'job_title', 'category', 'status', 'location'
    )

    job_rows = (", ".join(job) for job in values)

    return HttpResponse("\n".join(job_rows))
