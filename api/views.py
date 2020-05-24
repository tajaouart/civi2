# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('api/index.html')
    context = {
        'latest_question_list': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))

