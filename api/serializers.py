from rest_framework import serializers

from .models import CvJSON, Article
from django.http import HttpResponse


# class CVSerializer(serializers.HyperlinkedModelSerializer):
#     # json = serializers.CharField()
#     class Meta:
#         model = CvJSON
#         fields = ('json',)


class CVSerializer(serializers.Serializer):
    
    json = serializers.CharField()
    def create(self, cv: CvJSON):
        pass
    

        
class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'description', 'body', 'author_id')

    # title = serializers.CharField(max_length=120)
    # description = serializers.CharField()
    # body = serializers.CharField()
    # author_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)