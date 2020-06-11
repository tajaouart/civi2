from django.db import models


class Project():
    description : models.CharField()
    skills : models.CharField()


class Experience():
    project: [Project]


class Language():
    name : models.CharField()
    level :models.CharField()


class Contact():
    mail: models.CharField()
    tel: models.CharField()
    linkedin: models.CharField()
    website: models.CharField()
    interests: models.CharField()


class PersonalInformation():
    name: models.CharField()
    status: models.CharField()
    adress: models.CharField()
    born_in: models.CharField()
    birthday: models.CharField()
    contact: Contact


class Studie():
    year: models.CharField()
    description: models.CharField()


class CV():
    personal_information: PersonalInformation
    studies: [Studie]
    languages: [Language]
    experiences: Experience


class CvJSON(models.Model):
    json = models.CharField(max_length=10000)

    def __str__(self):
        return self.json


class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

