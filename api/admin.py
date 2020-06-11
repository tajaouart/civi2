# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CvJSON, Article, Author

# Register your models here.
admin.site.register(CvJSON)
admin.site.register(Article)
admin.site.register(Author)