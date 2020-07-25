import weasyprint as weasyprint
from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
from django.template import loader
from django.template.loader import render_to_string
from rest_framework import status, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from my_cv.settings import MEDIA_ROOT, MEDIA_URL
from .models import ProfilePhoto, CvJSON
from .serializers import FileSerializer, CVSerializer
from django.views.decorators.csrf import csrf_exempt


name_tag = "[%name%]"
image_tag = "[%image%]"
status_tag = "[%status%]"

ADRESS = """"<div class="side_subtitle">LIEU DE RESIDENCE :</div>
            <div class="side_body">[%adress%]</div> """
adress_tag = "[%adress%]"

BORN_IN = """"<div class="side_subtitle">LIEU DE NAISSANCE :</div>
            <div class="side_body">[%born_in%]</div>"""
born_in_tag = "[%born_in%]<"

BIRTHDAY = """<div class="side_subtitle">DATE DE NAISSANCE :</div>
            <div class="side_body">[%birthday%]</div>"""
birthday_tag = "[%birthday%]"

MAIL = """ <div class="side_body">[%mail%]</div>"""
mail_tag = "[%mail%]"

LINKEDIN = """<div class="side_body">[%linkedin%]</div>"""
linkedin_tag = "[%linkedin%]"

TEL = """<div class="side_body">[%tel%]</div>"""
tel_tag = "[%tel%]"

INTEREST = """<div class="side_body">[%interest%]</div>"""
interest_tag = "[%interest%]"

STUDY = """<li>[%study%]</li> """
study_tag = "[%study%]"

SKILL = """<li>[%skill%] </li>"""
skill_tag = "[%skill%]"

LANGUAGE = """<li>[%language%] </li>"""
language_tag = "[%language%]"

PROJECT = """
                <li> <b  class="orange">[%PROJECT_NAME%] :</b>
                   <ul>
                       <li>
                           [%PROJECT_DESCRIPTION%] :

                       </li>

                       <ul>
                       <li>
                           <b>[%PROJECT_SKILLS%]</b>
                       </li>
                       </ul>

                    </ul>
                </li>"""
project_tag = "[%project%]"
project_name_tag = "[%PROJECT_NAME%]"
project_description_tag = "[%PROJECT_DESCRIPTION%]"
project_skills_tag = "[%PROJECT_SKILLS%]"

html = ""


def index(request):
    photo = ProfilePhoto.objects.get(pk=16)
    photo_full_url = request.build_absolute_uri(photo.imageFile.url)
    context = {
        'photo': photo,
        'media_root': MEDIA_ROOT,
        'media_url': MEDIA_URL,
        'photo_full_url': photo_full_url,
    }

    template = loader.get_template('cv.html')
    html = render_to_string('cv.html', context)

    # html = CV.replace_data(html=html)

    # html_template = get_template('api/index.html')
    pdf_file = weasyprint.HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response


def set_in_comment(tag):
    return "<!--" + tag + "-->"


def replace(html, old, new):
    if not new and not old:
        return html
    else:
        return html.replace(old, new)


def oldindex(request):
    photo = ProfilePhoto.objects.all()[:1].get()
    template = loader.get_template('index.html')
    context = {
        'photo': photo,
        'media_root': MEDIA_ROOT,
        'media_url': MEDIA_URL
    }
    return HttpResponse(template.render(context, request))


def generat_cv(html, json_data):
    loaded_json = json.loads(json_data)

    personal_information = loaded_json['personal_information']
    studies = loaded_json['studies']
    languages = loaded_json['languages']
    experiences = loaded_json['experiences']
    skills = loaded_json['skills']
    interests = loaded_json['interests']
    image = ProfilePhoto.objects.all()[:1].get()

    # personal_information

    name = personal_information["name"]
    status = personal_information["status"]

    adress = personal_information["adress"]
    born_in = personal_information["born_in"]
    birthday = personal_information["birthday"]

    contact = personal_information["contact"]
    mail = contact["mail"]
    tel = contact["tel"]
    linkedin = contact["linkedin"]
    website = contact["website"]


    html = replace(html, set_in_comment(name_tag), name)
    html = replace(html, set_in_comment(status_tag), status)

    html = replace(html, set_in_comment(adress_tag), ADRESS.replace(adress_tag, adress))
    html = replace(html, set_in_comment(born_in_tag), BORN_IN.replace(born_in_tag, born_in))
    html = replace(html, set_in_comment(birthday_tag), BIRTHDAY.replace(birthday_tag, birthday))

    html = replace(html, set_in_comment(mail_tag), MAIL.replace(mail_tag, mail))
    html = replace(html, set_in_comment(tel_tag), TEL.replace(tel_tag, tel))
    html = replace(html, set_in_comment(linkedin_tag), LINKEDIN.replace(linkedin_tag, linkedin))

    # studies
    html_studies = ""
    for x in studies:
        _STUDY = STUDY
        html_studies += _STUDY.replace(study_tag, "<b>" + x + " : </b>" + studies[x])
    html = replace(html, set_in_comment(study_tag), html_studies)

    # interests
    html_interests = ""
    for x in interests:
        _INTEREST = INTEREST
        html_interests += _INTEREST.replace(interest_tag, x)
    html = replace(html, set_in_comment(interest_tag), html_interests)

    # languages
    html_languages = ""
    for x in languages:
        _LANGUAGE = LANGUAGE
        html_languages += _LANGUAGE.replace(language_tag, "<b>" + x + " : </b>" + languages[x])
    html = replace(html, set_in_comment(language_tag), html_languages)

    # skills
    html_skills = ""
    for x in skills:
        _SKILL = SKILL
        html_skills += _SKILL.replace(skill_tag, "<b>" + x + " : </b>" + skills[x])
    html = replace(html, set_in_comment(skill_tag), html_skills)

    # experiences
    html_experiences = ""

    for x in experiences:
        _PROJECT = PROJECT
        temp_html = _PROJECT.replace(project_name_tag, x)
        temp_html = temp_html.replace(project_description_tag, experiences[x]["description"])
        temp_html = temp_html.replace(project_skills_tag, experiences[x]["skills"])
        html_experiences += temp_html

    html = replace(html, set_in_comment(project_tag), html_experiences)

    return html


class CvViewSet(viewsets.ModelViewSet):
    queryset = CvJSON.objects.all()
    serializer_class = CVSerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def html(request):
    context = {
        'latest_question_list': 'latest_question_list',
    }
    template = loader.get_template('cv.html')
    html = HttpResponse(template.render(context, request)).content
    html.decode("utf-8")

    if request.method == "POST":
        pk = json.loads(request.body)['profile_photo_id']
        photo = ProfilePhoto.objects.get(pk=pk)
        photo_full_url = request.build_absolute_uri(photo.imageFile.url)
        context = {
            'photo': photo,
            'media_root': MEDIA_ROOT,
            'media_url': MEDIA_URL,
            'photo_full_url': photo_full_url,
        }
        html = generat_cv(template.render(context, request), request.body)
        pdf_file = weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="home_page.pdf"'
        return response

    else:
        return template.render(context, request)
