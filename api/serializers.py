from rest_framework import serializers

from .models import CvJSON, ProfilePhoto


class CVSerializer(serializers.Serializer):
    json = serializers.CharField()

    def create(self, cv: CvJSON):
        pass


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePhoto
        fields = "__all__"