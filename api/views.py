# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import weasyprint as weasyprint
from django.template import loader
from django.http import HttpResponse


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
    return HttpResponse(template.render(context, request))

