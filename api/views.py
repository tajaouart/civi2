# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import weasyprint as weasyprint
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import reportlab
from django.shortcuts import render


def index(request):
    template = loader.get_template('api/index.html')
    context = {
        'latest_question_list': 'latest_question_list',
    }
    html = HttpResponse(template.render(context, request)).content


    # html_template = get_template('api/index.html')
    pdf_file = weasyprint.HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response

    template = loader.get_template('api/index.html')
    context = {
        'latest_question_list': 'latest_question_list',
    }
    html =  HttpResponse(template.render(context, request)).content
    return HttpResponse(html)



def html(request):
    template = loader.get_template('api/index.html')
    context = {
        'latest_question_list': 'latest_question_list',
    }
    import ipdb;ipdb.sset_trace()
    return HttpResponse(template.render(context, request))

